from crewai import Task
from agents import researcher


research_task = Task(
    description=(
        "You are an expert academic researcher. Write comprehensive, well-organized study notes on '{topic}' "
        "that reflect deep understanding and practical relevance.\n\n"

        "**Structure:**\n"
        "1. **Overview & Context** - Why the topic matters\n"
        "2. **Core Concepts** - Key principles and definitions\n"
        "3. **Key Components** - Main elements with analysis\n"
        "4. **Applications** - Real-world use cases\n"
        "5. **Technical Details** - Methods, steps, or data\n"
        "6. **Current Trends** - Recent updates or innovations\n"
        "7. **Study Points** - Important facts for exams\n"
        "8. **Actionable Insights** - Practical tips or steps\n\n"

        "**Guidelines:**\n"
        "- Use **bold** for headers, *italics* for emphasis\n"
        "- Include examples, comparisons, and clear explanations\n"
        "- Use lists for processes or characteristics\n"
        "- Focus on clarity, depth (600-800), and logical flow\n"
        "- Highlight real-world relevance and common misconceptions\n\n"

        "These notes should serve as a complete reference for study or professional use, without needing extra resources."
    ),
    expected_output="Detailed, structured notes on the topic in a professional format.",
    agent=researcher,
    output_file="{topic}.docx"
)
