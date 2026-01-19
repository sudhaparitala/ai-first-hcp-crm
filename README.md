\# AI-First CRM – HCP Log Interaction Module



\## Overview

This project demonstrates an AI-first CRM system focused on logging interactions with Healthcare Professionals (HCPs) for life sciences field representatives.



\## Tech Stack

\- Frontend: React (conceptual)

\- Backend: FastAPI (Python)

\- AI Agent Framework: LangGraph

\- LLM: Groq (gemma2-9b-it)

\- Database: SQL (conceptual)

\- Font: Google Inter



\## Log Interaction Screen

The system allows users to log HCP interactions using:

1\. Structured form-based input

2\. Conversational chat-based interface powered by an AI agent



\## LangGraph Agent Role

The LangGraph agent acts as an orchestration layer that:

\- Interprets user intent

\- Routes requests to appropriate tools

\- Manages interaction workflows



\## Tools Implemented

1\. Log Interaction – Captures and summarizes HCP interaction notes

2\. Edit Interaction – Updates previously logged interactions

3\. Interaction History – Retrieves past HCP interactions

4\. Follow-Up Suggestions – Recommends next actions for field reps

5\. Compliance Check – Ensures interaction notes follow compliance guidelines



\## API Endpoints

\- POST /agent/chat

\- POST /interaction/log

\- POST /interaction/edit

\- GET /interaction/history

\- GET /interaction/followup

\- POST /interaction/compliance



\## Learning Summary

Through this assignment, I learned how AI agents using LangGraph can support CRM workflows in life sciences by integrating LLM-driven intelligence with backend APIs.



