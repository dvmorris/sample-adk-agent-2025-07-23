from google.adk import agents

# Define a very basic ADK agent
basic_agent = agents.Agent(
    name="my_basic_agent",
    model="gemini-1.5-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
)