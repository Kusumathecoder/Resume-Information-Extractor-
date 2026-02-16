from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.document_loaders import PyPDFLoader
from pydantic import BaseModel, Field
import json

class ResumeSchema(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address")
    skills: list[str] = Field(description="List of technical skills")
    experience_years: int = Field(description="Total years of experience")
    education: list[str] = Field(description="Educational qualifications")

parser = JsonOutputParser(pydantic_object=ResumeSchema)

prompt = PromptTemplate(
    template="""
Extract the following information from the resume text.

Resume Text:
{resume_text}

{format_instructions}

IMPORTANT:
Return ONLY valid JSON.
Do not add explanations.
""",
    input_variables=["resume_text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

model = ChatOllama(
    model="llama3",   # Make sure you pulled this
    temperature=0
)

chain = prompt | model | parser

loader = PyPDFLoader("Kusuma_M_1SI22CI021_CSE-AIML_SIT.pdf")
documents = loader.load()

resume_text = "\n".join([doc.page_content for doc in documents])

try:
    result = chain.invoke({"resume_text": resume_text})
    print(json.dumps(result, indent=4))
except Exception as e:
    print("Parsing Error:", str(e))
