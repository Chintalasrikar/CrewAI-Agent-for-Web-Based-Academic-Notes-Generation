# 📘 CrewAI Agent for Web-Based Academic Notes Generation


An **AI-powered research assistant** that automates the process of gathering and synthesizing information from the web, processing it with state-of-the-art language models, and generating structured academic notes. This tool integrates advanced technologies like **LLaMA 3.3** via **Groq**, **Serper.dev** for web search, and **CrewAI** for task management.

### How It Works:

1. **Web Search via Serper.dev**:
   - The research assistant begins by searching the web for relevant, high-quality information based on a user-provided topic. It uses **Serper.dev**, a tool that helps fetch accurate and reliable results from academic articles, papers, and other trusted sources.

2. **Processing Information with LLaMA 3.3 via Groq**:
   - After gathering the necessary information, the assistant processes it using the **LLaMA 3.3 model** hosted on **Groq**. LLaMA 3.3 is an advanced language model that excels in understanding and synthesizing complex data, ensuring that the information is summarized accurately and effectively.

3. **Generating Structured Academic Notes via CrewAI**:
   - Once the information is processed, the system uses **CrewAI** to organize and generate detailed, professional-grade academic notes. These notes are well-structured, featuring numbered lists, **bold** headings, and *italicized* emphasis to highlight key points and concepts. The generated content is designed to be concise, informative, and suitable for academic purposes.

4. **Output**:
   - The generated notes are saved as a `.docx` file, ready for further use or sharing. The format includes clear organization with headings, subheadings, and actionable takeaways, ensuring that the content is easily digestible and usable for academic or professional needs.

This AI-powered system allows researchers, students, and professionals to automate the process of web research, saving time and providing high-quality, structured notes without the need for manual intervention.

---

## 🚀 Features

- 🌐 Real-time web search using Serper.dev
- 🧠 Large Language Model (LLaMA 3.3 70B) via Groq
- 🤖 CrewAI-powered agent architecture
- 📝 Automatically generates academic-style research notes
- 💾 Saves the output as a `.docx` file

---

## 🛠️ Tech Stack

- Python
- [CrewAI](https://www.crewai.com/)
- [Groq](https://console.groq.com/) (LLaMA 3.3-70B model)
- [Serper.dev](https://serper.dev/) for web search
- `python-dotenv` for secure environment variables

---


## 📂 Project Structure

├── agents.py # Defines the Web Researcher agent
├── crew.py # Manages the CrewAI setup and execution
├── tasks.py # Defines the research task and output format
├── tools.py # Integrates Serper search tool
├── .env # Stores API keys securely
├── requirements.txt # Project dependencies
├── README.md # Project documentation

---


---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Chintalasrikar/CrewAI-Agent-for-Web-Based-Academic-Notes-Generation.git
cd CrewAI-Agent-for-Web-Based-Academic-Notes-Generation

```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Set Up Environment Variables

GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key


### 4. Run the Project

```bash
python crew.py

```
