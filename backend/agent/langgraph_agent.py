from langgraph.graph import StateGraph

# Simple state to hold text
class AgentState(dict):
    pass

# Tool: Log interaction
def log_interaction_tool(state: AgentState):
    text = state.get("text", "")
    return {"result": f"Logged interaction: {text}"}

# Tool: Edit interaction
def edit_interaction_tool(state: AgentState):
    text = state.get("text", "")
    return {"result": f"Edited interaction: {text}"}

# Create LangGraph
graph = StateGraph(AgentState)

# Add nodes (tools)
graph.add_node("log_interaction", log_interaction_tool)
graph.add_node("edit_interaction", edit_interaction_tool)

# Entry point
graph.set_entry_point("log_interaction")

# Compile agent
agent = graph.compile()
