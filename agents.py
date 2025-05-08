from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
 model="groq/llama-3.3-70b-versatile",
 temperature=0.7,
 api_key=GROQ_API_KEY
)

researcher = Agent(
    role="Web Researcher",
    goal="Search the web for information on a given topic and generate detailed notes",
    backstory=(
        """An expert researcher skilled in finding and summarizing web content for academic purposes.
        You are expert in writing detailed notes on various topics.""",
    tools=[search_tool],
    llm=llm,
    verbose=True
)
