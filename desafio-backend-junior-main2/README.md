# Desafio Técnico - API de Projetos e Tarefas

Este projeto consiste em uma API RESTful desenvolvida com **FastAPI** e **PostgreSQL**, com foco na gestão de projetos e tarefas. Ele visa avaliar conhecimentos práticos em:

- Estruturação de APIs REST
- Relacionamentos entre entidades
- Boas práticas com FastAPI e SQLAlchemy
- Uso de UUIDs como identificadores
- Migrations com Alembic

---

## Tecnologias utilizadas

- Python 3.10+
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic
- Uvicorn
- Pytest (para testes)

---

## Estrutura do projeto

```
.
├── app/
│   ├── models/              # Modelos do banco de dados (A SER CRIADO)
│   │   ├── __init__.py
│   │   ├── project.py       # Modelo Project (A SER CRIADO)
│   │   └── task.py          # Modelo Task (A SER CRIADO)
│   ├── schemas/             # Schemas Pydantic (A SER CRIADO)
│   │   ├── __init__.py
│   │   ├── project.py       # Schemas para Project (A SER CRIADO)
│   │   └── task.py          # Schemas para Task (A SER CRIADO)
│   ├── routers/             # Rotas da API (A SER CRIADO)
│   │   ├── __init__.py
│   │   ├── projects.py      # Endpoints de projetos (A SER CRIADO)
│   │   └── tasks.py         # Endpoints de tarefas (A SER CRIADO)
│   ├── __init__.py
│   ├── database.py          # Configuração do banco
│   └── main.py              # Entrada principal da aplicação
├── migration/               # Migrations geradas com Alembic
│   ├── env.py               # Configuração do ambiente Alembic
│   └── script.py.mako       # Template para migrations
├── tests/                   # Testes automatizados (A SER CRIADO)
│   ├── __init__.py
│   ├── test_projects.py     # Testes para projetos (A SER CRIADO)
│   └── test_tasks.py        # Testes para tarefas (A SER CRIADO)
├── alembic.ini              # Configuração do Alembic
├── requirements.txt         # Dependências
├── docker-compose.yml       # Configuração Docker para PostgreSQL
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md
```

---

## Requisitos

- Python 3.10+
- PostgreSQL
- (Opcional) Docker e Docker Compose

---

## Instalação e execução

### Opção 1: Usando Docker (Recomendado)

1. **Clonar o repositório**
```bash
git clone https://github.com/seu-usuario/api-projetos-tarefas.git
cd api-projetos-tarefas
```

2. **Iniciar o PostgreSQL com Docker**
```bash
docker-compose up -d
```

3. **Criar e ativar um ambiente virtual**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

4. **Instalar as dependências**
```bash
pip install -r requirements.txt
```

5. **Configurar variáveis de ambiente**
Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/desafio_db
```

6. **Implementar os modelos, schemas e routers** (ver seção abaixo)

7. **Rodar as migrations**
```bash
alembic upgrade head
```

8. **Iniciar o servidor**
```bash
uvicorn app.main:app --reload
```

### Opção 2: PostgreSQL local

1. **Instalar PostgreSQL localmente**
2. **Criar um banco de dados**
3. **Configurar a URL de conexão no arquivo `.env`**
4. **Seguir os passos 3-8 da Opção 1**

---

## Implementação necessária

### 1. Modelos (app/models/)

Crie os seguintes arquivos:

#### `app/models/project.py`
```python
# Modelo Project com:
# - id (UUID, primary key)
# - name (String, obrigatório)
# - description (Text, opcional)
# - created_at (DateTime)
# - updated_at (DateTime)
# - Relacionamento com Task (1:N)
```

#### `app/models/task.py`
```python
# Modelo Task com:
# - id (UUID, primary key)
# - title (String, obrigatório)
# - description (Text, opcional)
# - completed (Boolean, default False)
# - created_at (DateTime)
# - updated_at (DateTime)
# - project_id (UUID, foreign key para Project)
# - Relacionamento com Project (N:1)
```

### 2. Schemas (app/schemas/)

Crie os seguintes arquivos:

#### `app/schemas/project.py`
```python
# Schemas para Project:
# - ProjectBase (campos básicos)
# - ProjectCreate (para criação)
# - ProjectUpdate (para atualização)
# - Project (resposta completa)
# - ProjectWithTasks (inclui lista de tarefas)
```

#### `app/schemas/task.py`
```python
# Schemas para Task:
# - TaskBase (campos básicos)
# - TaskCreate (para criação, inclui project_id)
# - TaskUpdate (para atualização)
# - Task (resposta completa)
```

### 3. Routers (app/routers/)

Crie os seguintes arquivos:

#### `app/routers/projects.py`
```python
# Endpoints para projetos:
# - POST /projects/ (criar)
# - GET /projects/ (listar com paginação)
# - GET /projects/{project_id} (detalhar)
# - PUT /projects/{project_id} (atualizar)
# - DELETE /projects/{project_id} (deletar)
```

#### `app/routers/tasks.py`
```python
# Endpoints para tarefas:
# - POST /tasks/ (criar, validar se projeto existe)
# - GET /tasks/ (listar com paginação)
# - GET /tasks/{task_id} (detalhar)
# - PUT /tasks/{task_id} (atualizar)
# - DELETE /tasks/{task_id} (deletar)
```

### 4. Atualizar main.py

Adicione as importações e configurações necessárias:

```python
# Importar routers
from app.routers import projects, tasks

# Incluir routers
app.include_router(projects.router)
app.include_router(tasks.router)

# Criar tabelas (opcional, se não usar migrations)
from app.database import engine
from app.models import project, task
project.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)
```

### 5. Configurar migrations

Atualize `migration/env.py` para importar os modelos:

```python
from app.database import Base
from app.models import project, task
target_metadata = Base.metadata
```

### 6. Testes (tests/)

Crie testes para validar a funcionalidade:

#### `tests/test_projects.py`
```python
# Testes para endpoints de projetos
```

#### `tests/test_tasks.py`
```python
# Testes para endpoints de tarefas
```

---

## Documentação da API

Após a implementação, a documentação interativa estará disponível em:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

---

## Funcionalidades esperadas

### Projetos

- `POST /projects` - Criar projeto
- `GET /projects` - Listar projetos (com paginação)
- `GET /projects/{project_id}` - Detalhar projeto (inclui tarefas)
- `PUT /projects/{project_id}` - Atualizar projeto
- `DELETE /projects/{project_id}` - Deletar projeto

### Tarefas

- `POST /tasks` - Criar tarefa vinculada a um projeto
- `GET /tasks` - Listar tarefas (com paginação)
- `GET /tasks/{task_id}` - Detalhar tarefa
- `PUT /tasks/{task_id}` - Atualizar tarefa
- `DELETE /tasks/{task_id}` - Deletar tarefa

### Endpoints adicionais

- `GET /` - Informações da API
- `GET /health` - Verificação de saúde da API

---

## Exemplos de uso

### Criar um projeto
```bash
curl -X POST "http://localhost:8000/projects/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Meu Projeto", "description": "Descrição do projeto"}'
```

### Criar uma tarefa
```bash
curl -X POST "http://localhost:8000/tasks/" \
     -H "Content-Type: application/json" \
     -d '{"title": "Minha Tarefa", "description": "Descrição da tarefa", "project_id": "uuid-do-projeto"}'
```

### Listar projetos
```bash
curl -X GET "http://localhost:8000/projects/"
```

---

## Testes

Para rodar os testes automatizados (após implementação):

```bash
pytest
```

Para rodar com mais detalhes:
```bash
pytest -v
```

Para rodar com cobertura:
```bash
pytest --cov=app
```

---

## Migrations

### Criar uma nova migration
```bash
alembic revision --autogenerate -m "Descrição da mudança"
```

### Aplicar migrations
```bash
alembic upgrade head
```

### Reverter migration
```bash
alembic downgrade -1
```

---

## Critérios de avaliação

- **Estrutura do código**: Organização, legibilidade, boas práticas
- **Funcionalidade**: Todos os endpoints funcionando corretamente
- **Validação**: Uso adequado de Pydantic para validação
- **Relacionamentos**: Implementação correta dos relacionamentos entre entidades
- **Tratamento de erros**: Respostas HTTP apropriadas
- **Testes**: Cobertura de testes adequada
- **Documentação**: Documentação clara e completa

---

## Licença

Este projeto é fornecido apenas para fins de avaliação técnica.