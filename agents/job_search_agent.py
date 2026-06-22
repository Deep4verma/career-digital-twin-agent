import os
import json
from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# Load Digital Twin
# ==========================

with open("outputs/digital_twin.json", "r", encoding="utf-8") as f:
    twin = json.load(f)

career_goal = twin["career_goal"]

print("\n===== DIGITAL TWIN LOADED =====")
print(career_goal)

# ==========================
# Search Queries
# ==========================

search_queries = [
    career_goal,
    "Machine Learning Engineer",
    "AI Engineer",
    "Data Scientist",
    "Generative AI Engineer",
]

print("\nSearch Queries:")
print(search_queries)

# ==========================
# Apify Config
# ==========================

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN")

print("APIFY TOKEN =", APIFY_TOKEN)

if not APIFY_TOKEN:
    raise ValueError("APIFY_API_TOKEN not found in .env")

client = ApifyClient(APIFY_TOKEN)

# IMPORTANT:
# Replace with your actor id
ACTOR_ID = "cheap_scraper/linkedin-job-scraper"

all_jobs = []

# ==========================
# Search Jobs
# ==========================

for query in search_queries:

    print(f"\nSearching jobs for: {query}")

    run_input = {
        "keywords": [query],
        "location": "India",
        "maxItems": 150
    }

    try:

        run = client.actor(ACTOR_ID).call(
            run_input=run_input
        )

        dataset_id = run["defaultDatasetId"]

        for item in client.dataset(dataset_id).iterate_items():

            all_jobs.append(
                {
                    "job_title": item.get("jobTitle"),
                    "company": item.get("companyName"),
                    "location": item.get("location"),
                    "experience_level": item.get("experienceLevel"),
                    "job_url": item.get("jobUrl"),
                    "description": item.get("jobDescription", ""),
                    "matched_keywords": item.get(
                        "matchedKeywords", []
                    ),
                    "match_percentage": item.get(
                        "keywordMatchScorePercentage", 0
                    ),
                }
            )

        print(f"Collected {len(all_jobs)} jobs")

    except Exception as e:

        print(f"Error searching {query}")
        print(e)

# ==========================
# Remove Duplicates
# ==========================

unique_jobs = {}

for job in all_jobs:

    key = (
        f"{job['job_title']}_"
        f"{job['company']}"
    )

    unique_jobs[key] = job

all_jobs = list(unique_jobs.values())

print("\n===== FINAL STATS =====")
print("Total Unique Jobs:", len(all_jobs))

# ==========================
# Save Jobs
# ==========================

os.makedirs("outputs", exist_ok=True)

with open(
    "outputs/linkedin_jobs.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_jobs,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nJobs saved successfully!")
print("outputs/linkedin_jobs.json")