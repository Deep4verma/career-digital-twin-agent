from pydantic import BaseModel
import json
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
import os
load_dotenv()
import os

print(os.path.exists("data/memory/deepti_verma.json"))

# ==========================================
# OUTPUT SCHEMA
# ==========================================

class DigitalTwin(BaseModel):

    career_goal: str

    skill_level: str

    expertise_scores: dict

    current_focus: str

    learning_direction: str

    learning_evolution: list

    new_skills_detected: list

    profile_changes: list

    future_specialization: str

    future_career_path: list

    recommended_next_skills: list

    confidence_score: int

    reasoning: str


# ==========================================
# LOAD RESUME PROFILE
# ==========================================

with open("outputs/resume_profile.json", "r") as f:
    resume_profile = json.load(f)


# ==========================================
# LOAD MEMORY
# ==========================================

USER_NAME = "abheet_sonker"

memory_file = f"data/memory/{USER_NAME}.json"

print("Loading memory from:")
print(memory_file)   # later dynamic

memory_file = f"data/memory/{USER_NAME}.json"

with open(memory_file, "r") as f:
    memory_data = json.load(f)

history = memory_data["history"]

latest_state = history[-1]

if len(history) > 1:
    previous_state = history[-2]
else:
    previous_state = None
print("\n===== MEMORY DATA =====\n")
print(memory_data)

print("\n===== HISTORY LENGTH =====")
print(len(history))

print("\n===== LATEST STATE =====")
print(latest_state)

print("\n===== PREVIOUS STATE =====")
print(previous_state)


# ==========================================
# DIGITAL TWIN AGENT
# ==========================================

digital_twin_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    output_schema=DigitalTwin,
    parse_response=True,
    structured_outputs=True,
    markdown=False,
)


response = digital_twin_agent.run(
    f"""
You are an AI Career Digital Twin Builder.

Your task is to build a continuously evolving Career Digital Twin.

=================================================

RESUME PROFILE

{resume_profile}

=================================================

CURRENT USER STATE

{latest_state}

=================================================

PREVIOUS USER STATE

{previous_state}

=================================================

COMPLETE LEARNING HISTORY

{history}

=================================================

Generate:

1. career_goal

2. skill_level

3. expertise_scores

4. current_focus

5. learning_direction

6. learning_evolution

7. new_skills_detected

8. profile_changes

9. future_specialization

10. future_career_path

11. recommended_next_skills

12. confidence_score

13. reasoning

=================================================

SCORING RULES

Assign expertise scores from 1-10.

Weighting:

1. Thesis Topic → Highest Weight
2. Internship Experience → High Weight
3. Major Projects → Medium Weight
4. Skills Section → Medium Weight
5. Education → Low Weight

Do not determine expertise only from frequency.

Infer expertise using actual evidence.

=================================================

CONTINUOUS LEARNING RULES

Compare current state with previous state.

Identify:

- New learning areas
- New interests
- New completed skills
- Shift in focus
- Growth in expertise
- Career evolution

Example:

Previous:

["Machine Learning"]

Current:

[
 "Machine Learning",
 "Agentic AI",
 "Agno Framework"
]

Then:

learning_evolution:

[
 "Machine Learning",
 "Agentic AI",
 "Agno Framework"
]

new_skills_detected:

[
 "Agentic AI",
 "Agno Framework"
]

profile_changes:

[
 "Shift toward Agentic AI"
]

=================================================

FUTURE CAREER PREDICTION RULES

Analyze the complete learning history.

Do not simply summarize.

Identify:

1. Learning direction
2. Learning consistency
3. Emerging specialization
4. Future career trajectory

Predict the most likely specialization
for the next 6-12 months.

Do not simply repeat the current role.

Infer future growth direction.

Examples:

LangChain + RAG + Vector Databases
→ Generative AI Engineer

CrewAI + AutoGen + LangGraph + MCP
→ Multi-Agent AI Engineer

Power BI + SQL + Analytics
→ Analytics Engineer

PySpark + Kafka + Airflow
→ Data Engineer

LSTM + Forecasting + Statistics
→ Forecasting Scientist

=================================================

Generate:

future_specialization

Example:

"Multi-Agent AI Engineer"

=================================================

Generate:

future_career_path

Example:

[
 "AI Engineer",
 "Generative AI Engineer",
 "Multi-Agent AI Engineer",
 "AI Architect"
]

=================================================

Generate:

recommended_next_skills

Example:

[
 "LangGraph",
 "MCP",
 "AutoGen",
 "Agent Memory",
 "Agent Evaluation"
]

=================================================

Generate:

confidence_score

Range: 0-100

Higher score if learning trajectory
is consistent over time.

=================================================

Reasoning must explain:

1. Expertise scores

2. Current focus

3. Learning evolution

4. Profile changes

5. Future specialization

6. Future career path

7. Recommended next skills

8. Confidence score

Return structured output only.
"""
)

# ==========================================
# PRINT
# ==========================================

print("\n===== DIGITAL TWIN =====\n")
print(response.content)

digital_twin = response.content


# ==========================================
# SAVE OUTPUT
# ==========================================

digital_twin_dict = {

    "career_goal":
        digital_twin.career_goal,

    "skill_level":
        digital_twin.skill_level,

    "expertise_scores":
        digital_twin.expertise_scores,

    "current_focus":
        digital_twin.current_focus,

    "learning_direction":
        digital_twin.learning_direction,

    "learning_evolution":
        digital_twin.learning_evolution,

    "new_skills_detected":
        digital_twin.new_skills_detected,

    "profile_changes":
        digital_twin.profile_changes,

    "future_specialization":
        digital_twin.future_specialization,

    "future_career_path":
        digital_twin.future_career_path,

    "recommended_next_skills":
        digital_twin.recommended_next_skills,

    "confidence_score":
        digital_twin.confidence_score,

    "reasoning":
        digital_twin.reasoning
}

with open(
    "outputs/digital_twin.json",
    "w"
) as f:

    json.dump(
        digital_twin_dict,
        f,
        indent=4
    )

print("\nDigital Twin Saved Successfully!")