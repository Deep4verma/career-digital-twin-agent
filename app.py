import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Career Digital Twin",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Career Digital Twin")

st.markdown(
    """
Build an evolving digital twin of your career profile.
"""
)

# =====================================================
# USER NAME
# =====================================================

user_name = st.text_input(
    "User Name",
    placeholder="Deepti Verma"
)

# =====================================================
# RESUME
# =====================================================

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# =====================================================
# CAREER GOAL
# =====================================================

career_goal = st.selectbox(
    "Career Goal",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Business Analyst",
        "Product Analyst",
        "Data Engineer",
        "Analytics Engineer",
        "Business Intelligence Developer",
        "BI Analyst",
        "MLOps Engineer",
        "LLM Engineer",
        "Generative AI Engineer",
        "Agentic AI Engineer",
        "NLP Engineer",
        "Computer Vision Engineer",
        "Research Scientist",
        "Software Engineer",
        "Backend Engineer",
        "Cloud Engineer",
        "Product Manager"
    ]
)

# =====================================================
# COMPLETED SKILLS
# =====================================================

completed_skills = st.multiselect(
    "Completed Skills",
    [
        "Python",
        "SQL",
        "Advanced SQL",
        "Power BI",
        "Tableau",
        "Excel",
        "Statistics",
        "Machine Learning",
        "Deep Learning",
        "Time Series Forecasting",
        "NLP",
        "Computer Vision",
        "PySpark",
        "Databricks",
        "Delta Lake",
        "Data Engineering",
        "AWS",
        "Azure",
        "GCP",
        "Docker",
        "Kubernetes",
        "RAG",
        "LangChain",
        "LlamaIndex",
        "Vector Databases",
        "Generative AI",
        "Agentic AI",
        "MLOps"
    ]
)

# =====================================================
# CURRENT LEARNING
# =====================================================

current_learning = st.multiselect(
    "Currently Learning",
    [
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Computer Vision",
        "Time Series Forecasting",
        "Generative AI",
        "Prompt Engineering",
        "LangChain",
        "LlamaIndex",
        "RAG",
        "Agentic AI",
        "Agno Framework",
        "CrewAI",
        "AutoGen",
        "MCP",
        "Vector Databases",
        "PySpark",
        "Databricks",
        "Data Engineering",
        "Airflow",
        "Kafka",
        "MLOps",
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "GCP","Langraph"
    ]
)

# =====================================================
# INTERESTS
# =====================================================

interests = st.multiselect(
    "Interests",
    [
        "Machine Learning",
        "Deep Learning",
        "Computer Vision",
        "NLP",
        "Generative AI",
        "Agentic AI",
        "Time Series Forecasting",
        "Data Analytics",
        "Business Analytics",
        "Data Engineering",
        "MLOps",
        "Cloud Computing",
        "Recommendation Systems",
        "AI Agents",
        "Prompt Engineering",
        "RAG",
        "Vector Databases",
        "Power BI",
        "SQL",
        "Research",
        "Open Source",
        "Startups"
    ]
)

# =====================================================
# PROJECTS
# =====================================================

projects = st.text_area(
    "Projects Built",
    placeholder="LSTM Forecasting, RAG Chatbot, GAN Project..."
)

# =====================================================
# GENERATE DIGITAL TWIN
# =====================================================

if st.button("Generate Digital Twin"):

    if user_name.strip() == "":
        st.error("Enter User Name")
        st.stop()

    if uploaded_file is None:
        st.error("Upload Resume First")
        st.stop()

    # -----------------------------
    # Save Resume
    # -----------------------------

    os.makedirs(
        "data/resumes",
        exist_ok=True
    )

    resume_path = os.path.join(
        "data/resumes",
        uploaded_file.name
    )

    with open(resume_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # -----------------------------
    # Current State
    # -----------------------------

    current_state = {
        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "career_goal": career_goal,
        "completed_skills": completed_skills,
        "current_learning": current_learning,
        "interests": interests,
        "projects": projects
    }

    # -----------------------------
    # Memory Folder
    # -----------------------------

    os.makedirs(
        "data/memory",
        exist_ok=True
    )

    memory_file = (
        f"data/memory/"
        f"{user_name.lower().replace(' ','_')}.json"
    )

    previous_state = None

    # -----------------------------
    # Existing User
    # -----------------------------

    if os.path.exists(memory_file):

        with open(memory_file, "r") as f:
            memory_data = json.load(f)

        history = memory_data["history"]

        if len(history) > 0:
            previous_state = history[-1]

    else:

        history = []

    # -----------------------------
    # Add Current Session
    # -----------------------------

    history.append(current_state)

    memory_data = {
        "user_name": user_name,
        "history": history
    }

    with open(memory_file, "w") as f:

        json.dump(
            memory_data,
            f,
            indent=4
        )

    st.success(
        "Memory Updated Successfully!"
    )

    # =====================================================
    # CONTINUOUS LEARNING ANALYSIS
    # =====================================================

    st.subheader(
        "🧠 Continuous Learning Analysis"
    )

    if previous_state:

        old_learning = set(
            previous_state["current_learning"]
        )

        new_learning = set(
            current_learning
        )

        added_skills = list(
            new_learning - old_learning
        )

        removed_skills = list(
            old_learning - new_learning
        )

        old_interests = set(
            previous_state["interests"]
        )

        new_interests = set(
            interests
        )

        new_interests_added = list(
            new_interests - old_interests
        )

        st.write(
            "Previous Learning:",
            previous_state["current_learning"]
        )

        st.write(
            "Current Learning:",
            current_learning
        )

        st.write(
            "New Skills Added:",
            added_skills
        )

        st.write(
            "Skills Removed:",
            removed_skills
        )

        st.write(
            "New Interests Added:",
            new_interests_added
        )

        if len(added_skills) > 0:

            st.success(
                "🚀 Digital Twin Evolution Detected"
            )

    else:

        st.info(
            "First User Session Created"
        )

    # =====================================================
    # HISTORY
    # =====================================================

    st.subheader(
        "📚 Learning History"
    )

    st.json(history)

    st.subheader(
        "💾 Current Memory File"
    )

    st.json(memory_data)
    # =====================================================
# DIGITAL TWIN RESULTS
# =====================================================

if os.path.exists("outputs/digital_twin.json"):

    st.markdown("---")

    st.header("🚀 AI Career Digital Twin Insights")

    with open(
        "outputs/digital_twin.json",
        "r"
    ) as f:

        twin = json.load(f)

    # ----------------------------------
    # Current Twin
    # ----------------------------------

    st.subheader("🧠 Current Digital Twin")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Career Goal",
            twin["career_goal"]
        )

    with col2:
        st.metric(
            "Skill Level",
            twin["skill_level"]
        )

    with col3:
        st.metric(
            "Confidence Score",
            f"{twin['confidence_score']}%"
        )

    # ----------------------------------
    # Expertise Scores
    # ----------------------------------

    st.subheader("📊 Expertise Scores")

    for skill, score in twin[
        "expertise_scores"
    ].items():

        st.write(
            f"**{skill}** : {score}/10"
        )

        st.progress(score / 10)

    # ----------------------------------
    # Learning Evolution
    # ----------------------------------

    st.subheader(
        "🔄 Learning Evolution"
    )

    for item in twin[
        "learning_evolution"
    ]:

        st.write(f"➡️ {item}")

    # ----------------------------------
    # Profile Changes
    # ----------------------------------

    st.subheader(
        "📈 Profile Changes"
    )

    for item in twin[
        "profile_changes"
    ]:

        st.success(item)

    # ----------------------------------
    # Future Specialization
    # ----------------------------------

    st.subheader(
        "🚀 Future Specialization"
    )

    st.info(
        twin[
            "future_specialization"
        ]
    )

    # ----------------------------------
    # Career Path
    # ----------------------------------

    st.subheader(
        "🛣 Predicted Career Path"
    )

    for step in twin[
        "future_career_path"
    ]:

        st.write(f"🎯 {step}")

    # ----------------------------------
    # Recommended Skills
    # ----------------------------------

    st.subheader(
        "🎯 Recommended Next Skills"
    )

    for skill in twin[
        "recommended_next_skills"
    ]:

        st.write(f"✅ {skill}")

    # ----------------------------------
    # Reasoning
    # ----------------------------------

    st.subheader(
        "🤖 AI Reasoning"
    )

    st.write(
        twin["reasoning"]
    )