import json
from fastapi import FastAPI

from llm_functions.memory_recall_assessment import memory_recall_assessment

app = FastAPI()

@app.get("/get_memory_recall_assessment_questions")
async def get_memory_recall_assessment_questions():
    questions_str = await memory_recall_assessment()
    data = json.loads(questions_str)
    return data