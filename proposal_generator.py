from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from agents.agents import RequirementAgent,RetrieveAgent,PreviousSolAgent,ProposalGenerator

class SalesState(TypedDict):
  client_email:str
  requirements:str
  retrieved_projects:str
  solution_projects:str
  final_proposal:str

agent_builder=StateGraph(SalesState)

agent_builder.add_node("RequirementAgent",RequirementAgent)
agent_builder.add_node('RetrieveAgent',RetrieveAgent)
agent_builder.add_node('PreviousSolAgent',PreviousSolAgent)
agent_builder.add_node('ProposalGenerator',ProposalGenerator)

agent_builder.add_edge(START,'RequirementAgent')
agent_builder.add_edge('RequirementAgent','RetrieveAgent')
agent_builder.add_edge('RetrieveAgent','PreviousSolAgent')
agent_builder.add_edge('PreviousSolAgent','ProposalGenerator')
agent_builder.add_edge('ProposalGenerator',END)

agent=agent_builder.compile()