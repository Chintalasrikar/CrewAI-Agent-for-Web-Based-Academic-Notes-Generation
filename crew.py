from crewai import Crew
from agents import researcher
from tasks import research_task
import tools

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

topic = input("Enter the topic to research: ").strip() or "machine learning"
print(f"Researching topic: {topic}")
result = crew.kickoff(inputs={"topic": topic})
print(result)
