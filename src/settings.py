from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# データベース設定
DATABASE_URL = "postgresql+psycopg2://python:python@localhost:5432/python_db"

# エンジンとセッションの設定
engine = create_engine(
    DATABASE_URL,
    echo=True
)
Session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
)

Base: DeclarativeMeta = declarative_base()
