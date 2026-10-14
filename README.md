Aaron AI Chatbot

A personal AI chatbot that answers questions using information from my documents. Built with Python, LangChain, OpenAI, and FAISS.

Live site: https://akrizikairesponse.com

Tech Stack

Python / Flask – Web application

OpenAI GPT-6 Luna (gpt-6-luna) – Chat model

OpenAI Embeddings – Document embeddings

LangChain – Retrieval and question-answering

FAISS – Local vector database

PythonAnywhere – Hosting

GitHub – Version control

How It Works

Documents are converted into embeddings and stored in FAISS.

A user submits a question through the Flask web interface.

LangChain retrieves relevant document passages.

The OpenAI model generates a response using the retrieved context.

Project Structure

chatbot/
├── app.py
├── chatbot.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── vectorstore/       # Local, excluded from Git
└── .gitignore

Configuration

Requires an OPENAI_API_KEY environment variable and a locally generated FAISS vector store.

API keys and personal source documents are excluded from GitHub.

Deployment

Hosted on PythonAnywhere. Code changes are managed through Git and GitHub, with application reloads performed through the PythonAnywhere dashboard.

Status

October 2026: Operational. Updated chat model from GPT-4o mini to GPT-6 Luna.

Repository

https://github.com/Laconius/aaron-chatbot