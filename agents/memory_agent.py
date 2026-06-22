import json


user_memory = {
    "career_goal": "AI/ML Engineer",

    "current_learning": "Agno Framework and Agentic AI",

    "interests": [
        "Agentic AI",
        "Generative AI",
        "Machine Learning",
        "Data Science",
        "Data Analytics",
        "Business Analytics",
        "Data Engineering",
        "Time Series Forecasting"
    ]
}


with open("data/memory/user_memory.json", "w") as f:
    json.dump(user_memory, f, indent=4)

print("Memory saved successfully!")