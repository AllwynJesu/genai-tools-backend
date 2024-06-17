from fastapi import FastAPI
from langserve import add_routes
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import uvicorn
from dotenv import load_dotenv, find_dotenv

from routers import gen_ai_tools

load_dotenv(find_dotenv())

app = FastAPI(
    title="GenAI Tools Backend API Server",
    version="1.0",
    description="APIs for GenAI Tools",
)

app.include_router(gen_ai_tools.tools_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to GenAI Tools API Server"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)