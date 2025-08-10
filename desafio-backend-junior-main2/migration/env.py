from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Importa Base e modelos
from app.database import Base
from app.models import project, task  # importa todos os models

# Configuração do Alembic
config = context.config

# Interpreta arquivo de log do Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadados para autogenerate
target_metadata = Base.metadata

# URL do banco
def get_url():
    return os.getenv("DATABASE_URL", "postgresql+psycopg2://Nakaya:Nakaya123@localhost:8000/desafio_db")


def run_migrations_offline():
    """Executa migrations no modo offline."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Executa migrations no modo online."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()