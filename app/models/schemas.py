from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum


class QueryStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class QueryType(str, Enum):
    ANALYSIS = "analysis"
    REPORT = "report"
    SEARCH = "search"
    PREDICTION = "prediction"



class QueryRequest(BaseModel):
    query_text: str = Field(..., min_length = 1, max_legnth = 1000)
    user_id = Optional[str] = None
    parameters = Optional[Dict[str, Any]] = None


class QueryResponse(BaseModel):
    id: int
    user_id = Optional[str]
    query_text = str
    query_type = Optional[str]
    status = QueryStatus
    intent = Optional[str]
    confidence_score = Optional[float]
    result = Optional[Dict[str, any]]
    created_at = datetime
    processed_at = Optional[datetime]
    completed_at = Optional[datetime]


class AIAnalysisResponse(BaseModel):
    intent: str
    confidence_score: float
    entities: List[str]
    parameters: Dict[str, Any]
    suggested_queries: List[str]


class DataResult(BaseModel):
    data: List[Dict[str, Any]]
    summary: Dict[str, Any]
    visulization_suggestion: List[str]