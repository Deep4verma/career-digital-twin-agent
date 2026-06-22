# Career Digital Twin Agent using Agno

## Problem Statement

Traditional job recommendation systems rely only on resumes and job descriptions. They ignore a user's learning journey, evolving interests, career goals, and future potential.

As a result, users receive static recommendations that fail to adapt as they learn new skills or shift career directions.

## Solution

This project implements a Career Digital Twin that continuously learns from user interactions and builds an evolving representation of a user's career profile.

The system tracks:

* Resume-based skills and experience
* Career goals
* Learning activities
* Interests
* Historical profile evolution

The Digital Twin then predicts future specialization, recommends next skills, and generates a personalized career trajectory.

## Architecture

### Agent 1: Resume Parser Agent

Extracts:

* Education
* Skills
* Projects
* Domains

from uploaded resumes using Agno and Groq.

### Agent 2: Digital Twin Builder Agent

Combines:

* Resume Profile
* User Memory
* Historical Learning Data

to create an evolving Career Digital Twin.

Outputs:

* Expertise Scores
* Learning Evolution
* Profile Changes
* Future Specialization
* Career Path Prediction
* Recommended Skills

## Continuous Learning

Unlike traditional systems, the Digital Twin stores historical user states.

Each interaction updates memory rather than replacing it.

This enables:

* Skill evolution tracking
* Interest evolution tracking
* Career direction prediction
* Future specialization forecasting

## Tech Stack

* Agno Framework
* Groq LLM
* Pydantic
* Streamlit
* Python

## Future Scope

* Job Matching Agent
* Skill Gap Analysis Agent
* Learning Roadmap Generator
* LinkedIn Job Recommendation Integration
