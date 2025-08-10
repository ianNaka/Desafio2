from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import project, task
from app.routers import project, task


app = FastAPI(
    title="API de Projetos e Tarefas",
    description="API RESTful para gestão de projetos e tarefas",
    version="1.0.0"
)
app.include_router(project.router)
app.include_router(task.router)
# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Endpoint raiz da API"""
    return {
        "message": "Bem-vindo à API de Projetos e Tarefas",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    """Endpoint para verificar a saúde da API"""
    return {"status": "healthy"} 