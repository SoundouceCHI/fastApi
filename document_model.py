from pydantic import BaseModel, Field


class DocumentModel(BaseModel):
    """Model to validate a document."""
    title: str
    content: str
    age: int = Field(default=18, gt=0 ,lt= 120)
    author: str = "Anonymous"
