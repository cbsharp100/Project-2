from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str

class SourceChunk(BaseModel):
    doc: str
    page: Optional[int] = None
    chunk_id: str
    snippet: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceChunk]
    grounded: bool
