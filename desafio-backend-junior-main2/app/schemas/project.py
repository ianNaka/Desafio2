from typing import Optional, List
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

from .task import Task  # Importa para o schema com tarefas


# Campos básicos (compartilhados)
class ProjectBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: Optional[str] = None


# Para criação
class ProjectCreate(ProjectBase):
    pass


# Para atualização
class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None


# Resposta completa
class Project(ProjectBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Permite leitura a partir de objetos ORM


# Resposta com lista de tarefas
class ProjectWithTasks(Project):
    tasks: List[Task] = []