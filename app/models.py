from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50, pattern="^[a-zA-Z0-9 ]+$")
