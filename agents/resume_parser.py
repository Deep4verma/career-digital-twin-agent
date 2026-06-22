import os
from typing import List
import json
from pydantic import BaseModel
from pypdf import PdfReader
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq


load_dotenv()


class ResumeProfile(BaseModel):
    education: List[str]
    skills: List[str]
    projects: List[str]
    domains: List[str]

    internship_experience: List[str]
    thesis_topic: str


def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":

    print("Current Working Directory:")
    print(os.getcwd())

    pdf_path = "data/Resumes/Deepti_Verma_data_Science.pdf"

    resume_text = extract_text_from_pdf(pdf_path)

    print("\nResume Loaded Successfully")
    print("\nCreating Resume Parser Agent...\n")

    parser_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    output_schema=ResumeProfile,
    parse_response=True,
    structured_outputs=True,
    markdown=False,
)

    response = parser_agent.run(
    f"""
Extract information from the resume.

Return structured data.

Fields:

1. education
2. skills
3. projects
4. domains
5. internship_experience
6. thesis_topic

Rules:

- Extract internship work separately.
- Extract thesis topic separately.
- For projects include only major projects.
- For domains infer technical domains from projects, internship and thesis.
- Do not hallucinate.

Resume:

{resume_text}
"""
)

    print("\n========== STRUCTURED OUTPUT ==========\n")
    print(response.content)
    profile = response.content

profile_dict = {
    "education": profile.education,
    "skills": profile.skills,
    "projects": profile.projects,
    "domains": profile.domains,
    "internship_experience": profile.internship_experience,
    "thesis_topic": profile.thesis_topic,
}

with open("outputs/resume_profile.json", "w") as f:
    json.dump(profile_dict, f, indent=4)

print("\nProfile saved successfully!")