from typing import Optional
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


# Campos básicos
class TaskBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    completed: bool = False


# Para criação (inclui project_id)
class TaskCreate(TaskBase):
    project_id: UUID


# Para atualização
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    completed: Optional[bool] = None


# Resposta completa
class Task(TaskBase):
    id: UUID
    project_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Para suportar ORM