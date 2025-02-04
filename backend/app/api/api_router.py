from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from services.retrieval import RetrievalService
from services.generation import generate_response

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


class DocumentResponse(BaseModel):
    documents: List[str]


class GenerationResponse(BaseModel):
    answer: str


@router.post("/retrieve", response_model=DocumentResponse)
async def retrieve(query_request: QueryRequest):
    documents = RetrievalService.retrieve_documents(query_request.query)
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found")
    return DocumentResponse(documents=documents)


@router.post("/generate", response_model=GenerationResponse)
async def generate(query_request: QueryRequest):
    answer = generate_response(query_request.query)
    return GenerationResponse(answer=answer)
