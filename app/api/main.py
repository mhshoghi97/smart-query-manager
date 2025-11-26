from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db
from app.models.schemas import QueryRequest, QueryResponse, AIAnalysisResponse



app = FastAPI(title = "Smart Query Manager", description = "AI-powered query processing and analysis system", version = "1.0.0")


@app.get("/")
async def root():
    return {
        "message": "Smart Query Manager API is running",
        "version": "1.0.0",
        "endpoints": {
            "submit_query": "POST /queries/",
            "get_query": "GET /queries/{id}",
            "user_history": "GET /users/{id}/queries",
        }
    }