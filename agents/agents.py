from typing import TypedDict
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from retriever import load_vectorstore

vectorstore=load_vectorstore()

load_dotenv()

rag_llm=ChatGroq(model_name="llama-3.3-70b-versatile")
req_ext_llm=ChatGroq(model_name="llama-3.3-70b-versatile")
proposal_generator=ChatGroq(model_name='llama-3.3-70b-versatile')

class SalesState(TypedDict):
    client_email:str
    requirements:str
    retrieved_projects:str
    solution_approach:str
    final_proposal:str


def RetrieveAgent(state:SalesState):  
  requirements=state['requirements']
  retriever=vectorstore.as_retriever(search_type='similarity',search_kwargs={'k':3})
  res=retriever.invoke(requirements)

  final_doc=""
  for i in res:
    final_doc+=i.page_content
  return {'retrieved_projects':final_doc}


def PreviousSolAgent(state:SalesState):
  query=state['requirements']
  context=state['retrieved_projects']
  prompt=PromptTemplate(
    template="""

  You are a Solution Architect at XYZ Cloud Solutions.
  Analyze the new client requirement using the retrieved previous proposals.
  Your task is to identify the best approach to solve the client's problem.
  Do not write the final proposal. Only provide solution analysis.

  CLIENT REQUIREMENT:
  {query}

  SIMILAR PAST PROPOSALS:
  {context}

  PROVIDE ANALYSIS:

  1. Problem Understanding:
  - What is the client's main problem?
  - What business challenge needs to be solved?

  2. Relevant Previous Solutions:
  - Which past proposals are useful?
  - What ideas/components can be reused?

  3. Recommended Solution:
  Explain the proposed system and how it solves the problem.

  4. Technical Approach:
  Mention:
  - Frontend
  - Backend
  - AI/ML components
  - Database
  - Cloud

  5. Implementation Plan:
  Provide simple phases:
  - Requirement Analysis
  - Development
  - Testing
  - Deployment

  6. Expected Benefits:
  Mention improvements like:
  - Time saving
  - Cost reduction
  - Better efficiency

  Rules:
  - Use past proposals only as reference.
  - Do not copy them.
  - Keep the solution practical.
  - Do not generate the final proposal.
    """,input_variables=['query','context']
  )

  rag_chain=prompt | rag_llm | StrOutputParser()
  response=rag_chain.invoke({'query':query,'context':context})

  return {'solution_approach':response}

def RequirementAgent(state:SalesState):
  email=state['client_email']
  prompt=PromptTemplate(
      template="""

You are a Business Analyst working for XYZ Cloud Solutions.

Your task is to analyze the client email and extract the important business requirements.

Do not generate a proposal.
Do not suggest solutions.
Only identify and structure the client's needs.

CLIENT EMAIL:
{client_email}

EXTRACT REQUIREMENTS:
Extract the following information:

1. Client Industry:
Identify the business domain.

2. Business Problem:
What problem or inefficiency is the client facing?

3. Current Process:
Explain how the client currently handles this process.

4. Required Solution:
What type of system, product, or service does the client need?

5. Key Features/Functional Requirements:
List the expected capabilities.

6. Business Goals:
What outcome does the client want to achieve?

7. Timeline:
Extract project duration or expected delivery time.

8. Constraints:
Mention any limitations, integrations, security, or other requirements.

9. Priority:
Identify the most important requirement.

Return the output in a clear structured format.

Rules:
- Do not assume missing information.
- Do not invent requirements.
- Use only information available in the email.
- Keep the output concise and useful for downstream AI agents.

""",input_variables=['client_email']
  )

  req_ext_chain=prompt | req_ext_llm | StrOutputParser()
  response=req_ext_chain.invoke({'client_email':email})

  return {'requirements':response}

def ProposalGenerator(state:SalesState):
  solution_approach=state['solution_approach']
  requirements=state['requirements']

  prompt=PromptTemplate(
      template="""

You are a B2B sales proposal writer at XYZ Cloud Solutions.
Generate a professional client proposal using the client requirements and the recommended solution approach.
Do not mention internal AI workflow, agents, or previous proposals.

CLIENT REQUIREMENTS:
{requirements}

SOLUTION APPROACH:
{solution_approach}

CREATE PROPOSAL:
Generate a proposal with these sections:

XYZ Cloud Solutions Proposal
1. Executive Summary
   - Provides an overview of the client's requirement and the proposed solution to address their business needs.

2. Client Challenges
   - Describes the client's current problems, process inefficiencies, and business impact.

3. Proposed Solution
   - Explains the recommended solution, key features, and how it solves the client's challenges.

4. Solution Architecture
   - Defines the high-level technical design including system components, AI capabilities, integrations, and infrastructure.

5. Implementation Plan
   - Describes the execution phases required to build, test, and deploy the solution.

6. Timeline
   - Provides the estimated project duration and major implementation milestones.

7. Technology Stack
   - Lists the recommended technologies and platforms used to develop the solution.

8. Business Benefits
   - Highlights the expected improvements such as cost reduction, efficiency improvement, and better customer experience.

9. Assumptions
   - Specifies the dependencies, client inputs, and conditions required for successful implementation.

10. Next Steps
   - Defines the recommended actions after proposal review, such as discussions, approvals, and project initiation.

Rules:
- Keep it realistic and specific to the client.
- Use a professional business tone.
- Do not copy the solution approach directly.
- Generate only the final proposal.
""",input_variables=['requirements','solution_approach']
  )

  proposal_chain=prompt | proposal_generator | StrOutputParser()
  final_proposal=proposal_chain.invoke({'requirements':requirements,'solution_approach':solution_approach})

  return {'final_proposal':final_proposal}