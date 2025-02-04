# RAG System Backend

## Overview
The RAG System backend is built using FastAPI and is designed to handle document retrieval and response generation using large language models. It integrates with a vector database (FAISS) to efficiently search and retrieve relevant documents based on user queries.

## Project Structure
```
rag-system
├── backend
│   ├── app
│   │   ├── main.py             # Entry point for the FastAPI application
│   │   ├── api
│   │   │   └── endpoints.py    # API endpoints for handling requests
│   │   ├── core
│   │   │   └── config.py       # Configuration settings
│   │   ├── models
│   │   │   └── document.py      # Data model for documents
│   │   ├── services
│   │   │   ├── retrieval.py     # Logic for document retrieval
│   │   │   └── generation.py    # Logic for response generation
│   │   └── utils
│   │       └── faiss_helper.py  # Utility functions for FAISS
│   ├── requirements.txt         # Dependencies for the backend
│   └── README.md                # Documentation for the backend
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/dynamasoft/rag-system.git
   cd rag-system/backend
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Key Features
- **Document Retrieval**: Efficiently retrieves relevant documents using FAISS.
- **LLM Integration**: Generates responses based on retrieved documents using GPT-4.
- **Scalable Architecture**: Easily integrates with other vector databases like Pinecone, Weaviate, or ChromaDB.

## Usage
- Send a POST request to the defined API endpoints with your query to receive AI-generated responses based on the context retrieved from the document database.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.