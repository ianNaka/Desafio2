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
│   ├── models/              # Modelos do banco de dados 
│   │   ├── __init__.py
│   │   ├── project.py       # Modelo Project 
│   │   └── task.py          # Modelo Task 
│   ├── schemas/             # Schemas Pydantic 
│   │   ├── __init__.py
│   │   ├── project.py       # Schemas para Project
│   │   └── task.py          # Schemas para Task 
│   ├── routers/             # Rotas da API 
│   │   ├── __init__.py
│   │   ├── projects.py      # Endpoints de projetos 
│   │   └── tasks.py         # Endpoints de tarefas 
│   ├── __init__.py
│   ├── database.py          # Configuração do banco
│   └── main.py              # Entrada principal da aplicação
├── migration/               # Migrations geradas com Alembic
│   ├── env.py               # Configuração do ambiente Alembic
│   └── script.py.mako       # Template para migrations
├── tests/                   # Testes automatizados 
│   ├── __init__.py
│   ├── test_projects.py     # Testes para projetos 
│   └── test_tasks.py        # Testes para tarefas 
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

## Documentação da API
Após a implementação, a documentação interativa estará disponível em:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)


 Endpoints principais
Projetos
POST /projects → Criar projeto

GET /projects → Listar projetos

GET /projects/{id} → Detalhar projeto

PUT /projects/{id} → Atualizar projeto

DELETE /projects/{id} → Excluir projeto

--------------------------------------------------------------------------------------
Tarefas
POST /tasks → Criar tarefa

GET /tasks → Listar tarefas

GET /tasks/{id} → Detalhar tarefa

PUT /tasks/{id} → Atualizar tarefa

DELETE /tasks/{id} → Excluir tarefa

-------------------------------------------------------------

Licença
Projeto para fins de avaliação técnica.

