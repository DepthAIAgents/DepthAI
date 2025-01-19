import sys
import os

# Add the src folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '../src')
sys.path.append(src_path)

from agent import AgentManager

# Initialize the agent
api_key = os.getenv('OPENAI_API_KEY')
manager = AgentManager(api_key)

# Create two agents
agent1 = manager.create_agent("Assistant")
agent2 = manager.create_agent("Coder")

# Start a conversation with Agent 1
query = "What is the capital of France?"
response1 = agent1.send_message(query)
print(f"[Assistant]: {response1}")

# Continue talking to Agent 1
response2 = agent1.send_message("Can you tell me more about Paris?")
print(f"[Assistant]: {response2}")

# Start a conversation with Agent 2
response3 = agent2.send_message("Can you write a Python function to calculate Fibonacci numbers?")
print(f"[Coder]: {response3}")

# List all active agents
print("Active agents:", manager.list_agents())