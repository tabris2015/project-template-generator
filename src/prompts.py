from pydantic import BaseModel
from langchain import PromptTemplate

PROJECT_TEMPLATE = PromptTemplate.from_template(
    """You are an {major} senior student looking for a final project.
    In order to classify for your dissertation you need to present a project proposal with the following
    parts: 
    - Title
    - Hypothesis
    - Problem to solve
    - Justification
    - Main objective
    Generate {n_examples} examples for final projects with the given format in {language} language.
    """
)


class ProjectParams(BaseModel):
    major: str
    language: str
    n_examples: int
