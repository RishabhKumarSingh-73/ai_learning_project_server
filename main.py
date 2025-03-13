import json
import os
from fastapi import FastAPI
import uvicorn

from llm_functions.memory_recall_assessment import memory_recall_assessment

app = FastAPI()

@app.get("/get_memory_recall_assessment_questions")
async def get_memory_recall_assessment_questions():
    questions_str = await memory_recall_assessment()
    data = json.loads(questions_str)
    return data 

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if no PORT is assigned
    uvicorn.run(app, host="0.0.0.0", port=port)