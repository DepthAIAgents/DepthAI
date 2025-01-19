import openai
import json
import os
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize OpenAI API (ensure you have your API key set)
openai.api_key = "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"
Base = declarative_base()
DATABASE_URL = "sqlite:///agents.db"  # SQLite database file
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

class ChatGPTAgent:
    def __init__(self, name: str, model: str = "gpt-4"):
        self.name = name
        self.model = model
        self.conversation_history = []  # Initialize as empty, will load from file if needed

    def send_message(self, message: str) -> str:
        self.conversation_history.append({"role": "user", "content": message})
        
        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=self.conversation_history
            )
            assistant_message = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            return assistant_message
        except Exception as e:
            return f"Error: {e}"

class AgentManager:
    def __init__(self, db_file="agents.json"):
        self.db_file = db_file
        self.agents = self.load_agents()

    def load_agents(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                return json.load(f)
        return {}

    def save_agents(self):
        with open(self.db_file, "w") as f:
            json.dump(self.agents, f, indent=4)

    def create_agent(self, name: str, initial_query: str) -> ChatGPTAgent:
        if name in self.agents:
            raise ValueError(f"Agent with name '{name}' already exists.")
        print("creating")
        print(initial_query)
        # Create a new agent instance and send the initial query
        new_agent = ChatGPTAgent(name)
        initial_response = new_agent.send_message(initial_query)

        # Save the agent's data to the JSON file
        self.agents[name] = {
            "conversation_history": new_agent.conversation_history
        }
        self.save_agents()

        return new_agent, initial_response

    def get_agent(self, name: str) -> ChatGPTAgent:
        if name in self.agents:
            agent_data = self.agents[name]
            loaded_agent = ChatGPTAgent(name)
            loaded_agent.conversation_history = agent_data["conversation_history"]
            return loaded_agent
        else:
            raise ValueError(f"No agent found with name '{name}'.")

    def list_agents(self) -> list[str]:
        return list(self.agents.keys())
