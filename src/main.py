from fastapi import FastAPI, Depends
from src.llm_service import TemplateLLM
from src.prompts import ProjectParams
from src.parsers import ProjectIdeas

app = FastAPI()


def get_llm_service():
    return TemplateLLM()


@app.post("/generate")
def generate_project(params: ProjectParams, service: TemplateLLM = Depends(get_llm_service)) -> ProjectIdeas:
    return service.generate(params)


@app.get("/")
def root():
    return {"status": "OK"}
