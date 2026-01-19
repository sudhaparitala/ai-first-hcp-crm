# AI-First CRM – HCP Log Interaction Module

## Overview
This project demonstrates an AI-first Customer Relationship Management (CRM) system focused on logging interactions with Healthcare Professionals (HCPs) for life sciences field representatives.  
It integrates AI-driven automation for structured and conversational logging, compliance checking, and follow-up suggestions.

---

## Problem Statement
Field representatives face challenges in logging interactions efficiently and consistently.  
This system leverages AI (LangGraph + LLM) to:
- Capture HCP interactions accurately  
- Automate summarization  
- Suggest next best actions  
- Ensure compliance  

---

## Tech Stack
- **Frontend:** React + Redux (conceptual)  
- **Backend:** FastAPI (Python)  
- **AI Agent Framework:** LangGraph  
- **LLM:** Groq (gemma2-9b-it)  
- **Database:** SQL (MySQL/Postgres conceptual)  
- **Font:** Google Inter  

---

## Architecture / Workflow
User Input (Form / Chat)
↓
LangGraph AI Agent
↓
┌───────────────┐
│ 5 Tools │
│ - LogInteraction
│ - EditInteraction
│ - Interaction History
│ - Follow-Up Suggestions
│ - Compliance Check
└───────────────┘
↓
Database

## LangGraph Agent Role
The LangGraph agent orchestrates HCP interactions by:
- Interpreting user input (form or chat)  
- Routing requests to the correct tool  
- Maintaining HCP context  
- Ensuring compliance and suggesting next actions  

## Tools Implemented
1. Log Interaction – Captures and summarizes HCP interaction notes using LLM  
2. Edit Interaction – Updates previously logged interactions  
3. Interaction History – Retrieves past HCP interactions  
4. Follow-Up Suggestions – Recommends next actions for field reps  
5. Compliance Check – Ensures interaction notes follow compliance guidelines  

## Log Interaction Screen
- Structured Form Input: HCP name, specialty, product discussed, and follow-up info  
- Conversational Chat Input: AI extracts key fields from natural language input  
- Editing & Compliance: Users can edit interactions; AI validates compliance automatically  

## API Endpoints
- POST /agent/chat – Conversational AI input  
- POST /interaction/log – Save interaction  
- POST /interaction/edit – Edit interaction  
- GET /interaction/history – Retrieve past interactions  
- GET /interaction/followup – Get follow-up suggestions  
- POST /interaction/compliance – Compliance check  

## Learning Summary
- Learned how LangGraph orchestrates AI tools for CRM workflows  
- Applied LLM (Groq) for summarization and entity extraction  
- Designed modular APIs using FastAPI  
- Understood compliance and follow-up automation in HCP interactions  

## Instructions to Run

### Clone Repository
git clone https://github.com/sudhaparitala/ai-first-hcp-crm.git
cd ai-first-hcp-crm

### Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

### Frontend (conceptual)
- Run React dev server (if implemented)  
- Open http://localhost:3000 (or your configured port)

## Notes
- This project is conceptual in parts (frontend React and SQL database)  
- Focus is on demonstrating AI-first CRM workflows using LangGraph + LLM  
- Ensure all 5 tools are tested for video submission
