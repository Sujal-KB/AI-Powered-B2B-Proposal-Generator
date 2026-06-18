# AI-Powered B2B Proposal Generator

## Overview

The AI-Powered B2B Proposal Generator is an intelligent automation system that helps sales teams generate customized client proposals using Artificial Intelligence and Retrieval Augmented Generation (RAG).

In a traditional sales workflow, teams manually analyze client requirements, search previous proposals, design solution approaches, and create proposal documents. This process is time-consuming and often inconsistent.

This project automates the complete proposal generation workflow by using AI agents to understand client requirements, retrieve relevant past proposals, generate a suitable solution approach, and create a professional client-ready proposal.

---

# Problem Statement

Sales teams in B2B organizations receive client requirements through emails and manually perform the following tasks:

- Analyze client business requirements
- Identify customer challenges
- Search previous successful proposals
- Reuse relevant solution approaches
- Prepare customized proposals
- Review and modify documents before sending

This results in:

- Longer proposal preparation time
- Inconsistent proposal quality
- Difficulty in utilizing organizational knowledge
- Increased manual effort

---

# Proposed Solution

The proposed system uses multiple AI agents with a RAG-based knowledge retrieval system to automate proposal creation.

The system:

1. Extracts business requirements from client emails
2. Searches previous successful proposals using vector similarity search
3. Analyzes retrieved solutions
4. Creates a recommended technical approach
5. Generates a customized proposal document

---

# System Workflow

```
Client Email
      |
      ↓
Requirement Extraction Agent
      |
      ↓
Structured Client Requirements
      |
      ↓
RAG Retrieval System (FAISS)
      |
      ↓
Solution Analysis Agent
      |
      ↓
Proposal Generator Agent
      |
      ↓
Final Proposal Document
```

---

# AI Agents

## 1. Requirement Extraction Agent

Purpose:

Analyzes the client email and extracts important business information.

Extracts:

- Industry
- Business problem
- Current process
- Required solution
- Features
- Timeline
- Constraints

Example:

Input:

```
Need AI customer support automation system for banking.
Timeline: 6 months
```

Output:

```
Industry:
Banking

Problem:
High customer support workload

Solution:
AI-based customer support automation
```

---

## 2. Retrieval Agent (RAG)

Purpose:

Finds relevant previous successful proposals from the company knowledge base.

Technology:

- FAISS Vector Database
- HuggingFace Embeddings

Process:

```
Client Requirement

        ↓

Embedding Generation

        ↓

Similarity Search

        ↓

Relevant Past Proposals
```

---

## 3. Solution Analysis Agent

Purpose:

Acts as a Solution Architect.

It analyzes:

- Client requirements
- Retrieved proposals

and generates:

- Problem understanding
- Recommended solution
- Technical architecture
- Implementation approach
- Expected benefits

---

## 4. Proposal Generator Agent

Purpose:

Creates the final professional proposal.

Generated sections:

- Executive Summary
- Client Challenges
- Proposed Solution
- Solution Architecture
- Implementation Plan
- Timeline
- Technology Stack
- Business Benefits
- Assumptions
- Next Steps

---

# Technology Stack

## Programming Language

- Python

## AI Frameworks

- LangChain
- LangGraph

## Large Language Model

- Groq LLM
- Llama 3.3 70B

## Embedding Model

- Sentence Transformers

Model:

```
sentence-transformers/all-MiniLM-L6-v2
```

## Vector Database

- FAISS

## Environment Management

- Python-dotenv

---

# Project Structure

```
Assignment/

│
├── agents/
│   └── agents.py
│
├── data/
│   ├── proposal_1.txt
│   ├── proposal_2.txt
│   └── proposal_3.txt
│
├── proposal_faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── retriever.py
│
├── proposal_generator.py
│
├── create_vectorstore.py
│
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```
git clone <repository-url>
```

---

## 2. Install Dependencies

Create environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install packages:

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
```

---

# Creating Vector Database

Run this only when adding new proposal documents:

```
python create_vectorstore.py
```

This creates:

```
proposal_faiss_index/
```

containing the FAISS vector database.

---

# Running Application

Run:

```
streamlit run app.py
```

The system will:

1. Accept client email
2. Extract requirements
3. Retrieve similar proposals
4. Generate solution approach
5. Create final proposal

---

# Real World Impact

## Sales Team Benefits

- Reduces proposal preparation time
- Improves proposal consistency
- Reuses organizational knowledge
- Helps new sales employees create better proposals

## Business Benefits

- Faster client response
- Increased sales productivity
- Standardized proposal quality
- Reduced manual effort

---

# Future Improvements

Possible enhancements:

- Add email integration using Gmail/Outlook APIs
- Generate PDF proposals automatically
- Add human approval workflow
- Connect with CRM systems
- Add proposal quality evaluation agent
- Deploy as a web application using Streamlit/FastAPI

---

# Conclusion

This project demonstrates how AI agents and RAG can automate a real-world B2B sales workflow by transforming unstructured client emails into customized professional proposals while leveraging previous organizational knowledge.
