from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from crewai_tools import tool
from rag import kb_sem, kb_mic, kb_ari

@tool("RAG Tool for Semantic HTML Knowledge Base")
def sem_tool(question: str) -> list:
    """Only takes in a string as a question. Tool to search the Semantic HTML Knowledge Base using RAG."""
    return kb_sem.search(question, 10)

@tool("RAG Tool for Microdata & Schema Markup Knowledge Base")
def mic_tool(question: str) -> list:
    """Only takes in a string as a question. Tool to search the Microdata & Schema Markup Knowledge Base using RAG."""
    return kb_mic.search(question, 10)

@tool("RAG Tool for ARIA Text Knowledge Base")
def ari_tool(question: str) -> list:
    """Only takes in a string as a question. Tool to search the ARIA Text Knowledge Base using RAG."""
    return kb_ari.search(question, 10)

groq_llm = ChatGroq(
    model="mixtral-8x7b-32768",
    api_key="..."
)

backstory_data = 'This agent is designed to develop and improve code by implementing new features, optimizing performance, and ensuring functional correctness.'


CodeGenerator = Agent(
    role="Code Implementation Specialist",
    goal="Develop and improve the provided code according to the task by implementing new features, optimizing performance, and ensuring functional correctness. Here is the input code: {input}",
    verbose=True,
    llm=groq_llm,
    tools=[sem_tool, mic_tool, ari_tool],
    backstory=backstory_data,
    output = "Return code.")

SEM_Generator = Task(
    description="Add semantic HTML to the provided code",
    expected_output="Return code.",
    agent=CodeGenerator,
)

MIC_Generator = Task(
    description="Add microdata schema markup to the provided code",
    expected_output="Return code.",
    agent=CodeGenerator
)

ARI_Generator = Task(
    description="Add ARIA text to the provided code",
    expected_output="Return code.",
    agent=CodeGenerator
)

my_crew = Crew(agents=[CodeGenerator], tasks=[SEM_Generator, MIC_Generator, ARI_Generator])

input_code = '''<!DOCTYPE html>
<html>
<body>
<h1>My First Heading</h1>
<p>My first paragraph.</p>
</body>
</html>'''

crew_output = my_crew.kickoff(inputs={"input": input_code})
print(f"Raw Output: {crew_output.raw}")
