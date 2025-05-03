from fastapi import FastAPI, Request
from Essay_agent import create_graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

agent_graph = create_graph()

@app.post("/generate_essay")
async def generate_essay(request: Request):
    try:
        data = await request.json()
        topic = data.get("topic", "Pizza Shop")
        print(f"Received topic: {topic}")
        result = agent_graph.invoke({"topic": topic})
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Error during essay generation: {e}")
        return {"error": str(e)}
