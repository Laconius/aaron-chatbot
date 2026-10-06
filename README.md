Aaron Chatbot

A retrieval-augmented generation (RAG) chatbot built with Python, Flask, LangChain, FAISS, and the OpenAI API.

The application answers questions using a private knowledge base while combining semantic search with an OpenAI language model to generate natural-language responses.

How It Works

The application follows a basic RAG architecture:

User Question
      ↓
Flask Web Application
      ↓
OpenAI Embeddings
      ↓
FAISS Vector Search
      ↓
Relevant Knowledge Retrieved
      ↓
OpenAI Language Model
      ↓
Generated Answer

Rather than relying solely on information contained in the language model, the chatbot retrieves relevant information from a private document collection before generating its response.

Technology Stack

Python

Flask

LangChain

FAISS

OpenAI API

OpenAI Embeddings

HTML / CSS

PythonAnywhere

Project Structure

app.py

Runs the Flask web application and handles requests from the browser.

chatbot.py

Contains the RAG pipeline, including document embeddings, FAISS retrieval, and OpenAI model integration.

templates/

Contains the HTML interface.

static/

Contains CSS and other static website assets.

The private knowledge documents and generated FAISS vector database are intentionally excluded from this public repository.

Security

API credentials are stored in environment variables using a .env file.

The .env file is excluded from Git through .gitignore and should never be committed to a public repository.

Private source documents and the generated vector store are also excluded.

Running the Application

Create a Python virtual environment and install the required dependencies.

Create a .env file containing:

OPENAI_API_KEY=your_api_key_here

The application expects private knowledge documents to be available locally and uses them to build or load the FAISS vector store.

Run the Flask application:

python app.py

Current Model

The chatbot currently uses OpenAI gpt-4o-mini for response generation.

OpenAI embeddings are used to convert the private knowledge base and user queries into vector representations for semantic retrieval.

Purpose

This project was created as a practical exercise in building an AI-powered application using retrieval-augmented generation.

It demonstrates several concepts used in modern AI systems:

LLM API integration

Retrieval-augmented generation (RAG)

Vector embeddings

Semantic search

Vector databases

Environment-variable secret management

Flask web application development

Deployment of an AI application

Git/GitHub source control

Future Improvements

Potential improvements include:

Migrating to OpenAI's current Responses API

Model routing and automatic provider fallback

Support for multiple LLM providers

Improved observability and error logging

Automated model-deprecation monitoring

Conversation memory

Streaming responses

More sophisticated retrieval and ranking

Automated knowledge-base updates

Deployment

The current application is deployed using PythonAnywhere.

The public repository contains the application source code while API credentials, private knowledge documents, and vector indexes remain outside source control.
