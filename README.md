# Before Learning LangGraph, Build This AI Agent First

## Project Overview

This project documents my learning journey of building an AI Agent from scratch using Python and a local LLM (Ollama - Llama 3.2 3B), without using any AI orchestration frameworks such as LangGraph.

The objective of this lab was to understand the core building blocks of an AI Agent by implementing every feature manually. Instead of relying on orchestration frameworks, each capability was developed step-by-step to understand how enterprise AI Agents work internally.

This project is intended as a learning lab and architectural reference rather than a production-ready application.

---

# Solution Architecture

Customer --> Interactive Chat --> Intent classification -->Guardrail Check --> System Prompt --> Local LLM (Ollama) --> Native Tool Calling --> Python Business Logic --> Customer Policy (.csv) --> Response Generation --> Customer

---

# Technology Stack

- Python
- Ollama
- Llama 3.2 3B
- Visual Studio Code
- Git & GitHub
- Pandas
- CSV as Business Data Source

---

# Learning Objectives

This project was built to understand:

- Interactive AI conversations
- Conversation context
- Prompt Engineering
- Intent Classification
- Guardrails
- Native Tool Calling
- Reason → Act → Observe workflow
- Hallucination reduction
- Short-term conversation memory
- AI Agent architecture fundamentals

---

# Project Structure

```
project/
│
├── app.py
├── prompts.py
├── tools.py
├── data/
│   └── customer_data.csv
├── xtraFiles
└── README.md
```

---

# Version History

## Version 1 – Interactive Chat

### Objective

Build a simple command-line chatbot using Ollama.

### Skills Developed

- Interactive chat loop
- User input handling
- Local LLM integration

### Challenge

The application behaved only as a chatbot and had no conversation context.

---

## Version 2 – Conversation Context

### Objective

Maintain conversation history between user and AI.

### Skills Developed

- Conversation management
- Chat history
- Multi-turn interaction

### Challenge

The AI remembered previous messages but still had no business knowledge.

---

## Version 3 – System Prompt

### Objective

Define the AI Assistant's behaviour using a system prompt.

### Skills Developed

- Prompt Engineering
- Role definition
- Response control

### Challenge

Although responses became more consistent, the AI could still hallucinate policy information.

---

## Version 4 – Streaming Response

### Objective

Display responses as they are generated.

### Skills Developed

- Streaming output
- Improved user experience

### Challenge

Streaming improved usability but did not add business capabilities.

---

## Version 5 – Native Tool Calling

### Objective

Enable the AI Agent to execute Python functions.

### Skills Developed

- Tool definition
- Function schema
- Native tool calling
- Business data retrieval

### Challenge

The AI could retrieve policy data but still required better control over when tools should be used.

---

## Version 6 – Intent Classification & Guardrails

### Objective

Restrict the AI Agent to insurance-related queries.

### Skills Developed

- Intent classification
- Domain restriction
- Guardrail implementation

### Challenge

Simple keyword-based intent classification works for demonstrations but has limitations for enterprise scenarios.

---

## Version 7 – Reason → Act

### Objective

Implement the reasoning and action stages of an AI Agent.

### Skills Developed

- Tool selection
- Function execution
- Business logic integration

### Challenge

The AI Agent could execute tools but was still displaying raw tool output.

---

## Version 8 – Observe

### Objective

Generate customer-friendly responses using tool output.

### Skills Developed

- Multi-step LLM interaction
- Response generation
- Tool result interpretation

### Challenge

The LLM occasionally added information that was not present in the business data.

---

## Version 9 – Hallucination Reduction

### Objective

Reduce hallucinations using stricter prompting.

### Skills Developed

- Prompt refinement
- Controlled response generation
- Output validation

### Challenge

Although hallucinations were significantly reduced, prompt engineering alone cannot eliminate them completely.

---

## Current Version

### Additional Improvements

- Short-term conversation memory
- Cleaner project structure
- Modular Python files
- Improved prompt design
- Better user experience
- Reduced debugging output

---

# Engineering Challenges Encountered

| Challenge 						| Resolution |
|-----------------------------------|------------|
| No conversation context 			| Added conversation history |
| AI had no business knowledge 		| Introduced native tool calling |
| AI answered unrelated questions 	| Added intent classification and guardrails |
| Raw tool output 					| Introduced response generation stage |
| Hallucinated responses 			| Strengthened prompts and constrained responses |
| Large monolithic application 		| Modularised into multiple Python files |
| Limited conversation continuity 	| Added short-term memory |

---

# Key AI Engineering Concepts Demonstrated

- Interactive AI Chat
- Prompt Engineering
- Context Management
- Intent Classification
- Guardrails
- Native Tool Calling
- Business Logic Integration
- Reason → Act → Observe
- Hallucination Reduction
- Short-term Memory
- Modular AI Agent Design

---

# Key Learning

Building an AI Agent manually provides a clear understanding of how LLMs interact with tools, business logic and application workflows.

As additional capabilities such as authentication, multiple tools, memory, approvals and external APIs are introduced, the application logic becomes increasingly complex. Managing these workflows using plain Python requires additional effort in state management, conditional routing and debugging.

This is where AI workflow orchestration frameworks such as **LangGraph** become valuable. Rather than improving the reasoning capability of the LLM, they simplify workflow orchestration by managing state, routing, multi-step execution and communication between different components of an AI Agent.

Understanding these fundamentals first makes it much easier to adopt orchestration frameworks for building production-ready AI applications.

---

## Author

**Aman Khan**
Solution Architect 
