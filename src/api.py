from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import sys
import os

# Add the src folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '../src')
sys.path.append(src_path)

from agent import AgentManager

# Initialize FastAPI app and AgentManager
app = FastAPI()
api_key = "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"
manager = AgentManager(api_key)

# Request and Response Models
class CreateAgentRequest(BaseModel):
    name: str
    initial_query: str  # Added initial query for agent initialization

class MessageRequest(BaseModel):
    agent_name: str
    message: str

class ListAgentsResponse(BaseModel):
    agents: list[str]

# Endpoints
@app.post("/agents", response_model=dict)
def create_agent(request: CreateAgentRequest):
    """
    Create a new agent with an initial query.
    """
    try:
        # Create the agent
        
        # Send the initial query to the agent
        #initial_response = agent.send_message(request.initial_query)
        agent,rese = manager.create_agent(request.name,request.initial_query)

        return {
            "message": f"Agent '{request.name}' created successfully.",
            "initial_response": rese  # Include the initial response
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/agents", response_model=ListAgentsResponse)
def list_agents():
    """
    List all active agents.
    """
    agents = manager.list_agents()
    return {"agents": agents}

@app.post("/agents/message", response_model=dict)
def send_message(request: MessageRequest):
    """
    Send a message to an agent and get a response.
    """
    try:
        agent = manager.get_agent(request.agent_name)
        response = agent.send_message(request.message)
        return {"response": response}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))