from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# データベース設定
DATABASE_URL = "postgresql+psycopg2://python:python@localhost:5432/python_db"

# エンジンとセッションの設定
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    age = Column(Integer)

# テーブルが存在しない場合は作成
Base.metadata.create_all(engine)

# Select関数
def select_user(user_id):
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            print(f"Found user: {user.id}, {user.name}, {user.age}")
        else:
            print("User not found")

# Create関数
def create_user(name, age):
    with Session() as session:
        user = User(name=name, age=age)
        session.add(user)
        session.commit()
        print(f"User created with id: {user.id}")

# Update関数
def update_user(user_id, name=None, age=None):
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            if name:
                user.name = name
            if age:
                user.age = age
            session.commit()
            print("User updated")
        else:
            print("User not found")

# Remove関数
def remove_user(user_id):
    with Session() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print("User removed")
        else:
            print("User not found")