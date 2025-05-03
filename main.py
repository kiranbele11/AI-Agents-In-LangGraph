from fastapi import FastAPI, Request
from Essay_agent import create_graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

agent_graph = create_graph()

@app.post("/generate_essay")
async def generate_essay(request: Request):
    data = await request.json()
    topic = data.get("topic", "Pizza Shop")
    result = agent_graph.invoke({"topic": topic})
    return result