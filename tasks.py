from crewai import Task
from agents import researcher


research_task = Task(
    description=(
        "Search the web for information on the topic '{topic}'. "
        "Generate detailed and well-structured notes on that topic. "
        "Use numbered lists to organize concepts, include examples where relevant, and end with actionable takeaways. "
        "Use Bold letters for headings and subheadings, and Italics for emphasis."
        "Use examples to illustrate key points and concepts."
        "Ensure the notes are concise, professional, and suitable for academic study."
        "write minimum of 2 pages of notes."
    ),
    expected_output="Detailed, structured notes on the topic in a professional format.",
    agent=researcher,
    output_file="{topic}.docx"
)
