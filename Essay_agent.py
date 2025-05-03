from typing import TypedDict
from langchain_core.runnables import Runnable
from langgraph.graph import StateGraph

# ✅ Define the expected state structure
class EssayState(TypedDict):
    topic: str
    plan: str
    research: str
    essay: str
    reflection: str
    critique: str

# === Node Functions ===
def planner_node(state):
    topic = state['topic']
    return {"topic": topic, "plan": f"Planning topic: {topic}", "next": "research_plan"}

def research_plan_node(state):
    plan = state['plan']
    return {"research": f"Deep research for: {plan}", "next": "generate"}

def generate_node(state):
    return {"essay": f"This is an essay draft on {state['topic']}...", "next": "reflect"}

def reflect_node(state):
    return {"reflection": f"Reviewing draft for {state['topic']}", "next": "research_critique"}

def research_critique_node(state):
    return {"critique": f"Critiquing the generated content on {state['topic']}", "next": None}

# === Create LangGraph ===
def create_graph():
    graph = StateGraph(state_schema=EssayState)  # ✅ Pass state schema

    graph.add_node("planner", Runnable(planner_node))
    graph.add_node("research_plan", Runnable(research_plan_node))
    graph.add_node("generate", Runnable(generate_node))
    graph.add_node("reflect", Runnable(reflect_node))
    graph.add_node("research_critique", Runnable(research_critique_node))

    graph.set_entry_point("planner")
    graph.add_edge("planner", "research_plan")
    graph.add_edge("research_plan", "generate")
    graph.add_edge("generate", "reflect")
    graph.add_edge("reflect", "research_critique")

    return graph.compile()
