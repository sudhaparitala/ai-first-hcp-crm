from fastapi import FastAPI
from pydantic import BaseModel

# Import LangGraph agent
from agent.langgraph_agent import agent

# Import tools
from tools.log_interaction import log_interaction
from tools.edit_interaction import edit_interaction
from tools.history_tool import get_interaction_history
from tools.followup_tool import generate_followup
from tools.compliance_tool import compliance_check

app = FastAPI()

class InteractionRequest(BaseModel):
    text: str

@app.post("/agent/chat")
def agent_chat(request: InteractionRequest):
    """
    Sends input text to LangGraph agent.
    """
    result = agent.invoke({"text": request.text})
    return result

@app.post("/interaction/log")
def log_interaction_api(request: InteractionRequest):
    return log_interaction(request.text)

@app.post("/interaction/edit")
def edit_interaction_api(request: InteractionRequest):
    return edit_interaction(1, request.text)

@app.get("/interaction/history")
def history_api():
    return get_interaction_history("Dr. Sample")

@app.get("/interaction/followup")
def followup_api():
    return generate_followup("Dr. Sample")

@app.post("/interaction/compliance")
def compliance_api(request: InteractionRequest):
    return compliance_check(request.text)
