from langchain.llms import OpenAI
from src.config import get_settings
from src.prompts import PROJECT_TEMPLATE, ProjectParams

_SETTINGS = get_settings()


class TemplateLLM:
    def __init__(self):
        self.llm = OpenAI(
            model_name=_SETTINGS.model, openai_api_key=_SETTINGS.openai_key
        )
        self.prompt_template = PROJECT_TEMPLATE

    def generate(self, params: ProjectParams):
        prompt = self.prompt_template.format(**params.dict())
        return self.llm.predict(prompt)

    def generate_and_save(self, params: ProjectParams, out_file: str):
        output = self.generate(params)
        with open(out_file, "w") as f:
            f.write(output)
