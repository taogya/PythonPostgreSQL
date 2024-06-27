from sqlalchemy import Column, Integer, Sequence, String

from settings import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    age = Column(Integer)
