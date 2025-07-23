import os
import vertexai
from vertexai.preview import reasoning_engines
from vertexai import agent_engines

PROJECT_ID = "heb-sandbox-abcd"
LOCATION = "us-central1"  # Or any other supported region
STAGING_BUCKET = "gs://heb-sandbox-abcd" # A Cloud Storage bucket for staging

from my_basic_agent.agent import basic_agent

def deploy_agent():
    vertexai.init(project=PROJECT_ID, location=LOCATION, staging_bucket=STAGING_BUCKET)

    agent_app = reasoning_engines.AdkApp(
        agent=basic_agent,
        enable_tracing=True
    )

    deployed_agent = agent_engines.create(
        agent_engine=agent_app,
        display_name="My First Deployed ADK Agent",
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]"   
        ],
        extra_packages=["./my_basic_agent"],
    )

    print("Deployment successful!")
    print(f"Deployed Agent Name: {deployed_agent.resource_name}")

if __name__ == "__main__":
    deploy_agent()