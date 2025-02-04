# Retrieval-Augmented Generation (RAG) System

This project is a Retrieval-Augmented Generation (RAG) System designed to enhance large language models (LLMs) like GPT-4 by integrating document search and retrieval capabilities. It aims to provide accurate answers to user queries by retrieving relevant information from a custom knowledge base before generating a response.

## Key Features

- **Document Retrieval**: Utilizes FAISS (a vector database) to find the most relevant information from stored documents.
- **LLM Integration**: Queries GPT-4 to generate responses based on the retrieved context using Langchain and Langgraph.
- **React Frontend**: Offers an interactive search UI for users to input questions and receive AI-generated answers.
- **FastAPI Backend**: Manages query processing, document search, and AI-generated responses.
- **Scalable & Customizable**: Can integrate with Pinecone, Weaviate, or ChromaDB for scalable vector search.

## Project Structure

```
rag-system
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── api
│   │   │   └── endpoints.py
│   │   ├── core
│   │   │   └── config.py
│   │   ├── models
│   │   │   └── document.py
│   │   ├── services
│   │   │   ├── retrieval.py
│   │   │   └── generation.py
│   │   └── utils
│   │       └── faiss_helper.py
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── src
│   │   ├── components
│   │   │   └── SearchBar.jsx
│   │   ├── pages
│   │   │   └── Home.jsx
│   │   ├── App.jsx
│   │   └── index.js
│   ├── package.json
│   └── README.md
├── docs
│   └── architecture.md
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd rag-system
   ```

2. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the FastAPI application:
     ```
     uvicorn app.main:app --reload
     ```

3. **Frontend Setup**:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm start
     ```

## Usage

- Access the frontend application at `http://localhost:3000`.
- Use the search bar to input queries and receive AI-generated responses based on the retrieved documents.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.