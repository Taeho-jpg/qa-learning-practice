from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Skill(Base):
    __tablename__ = "skills"

    id    = Column(Integer, primary_key=True, index=True)
    name  = Column(String, nullable=False)
    level = Column(String, nullable=False)

class Todo(Base):
    __tablename__ = "todos"

    id    = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    done  = Column(Boolean, default=False)

class Book(Base):
    __tablename__ = "books"

    id     = Column(Integer, primary_key=True, index=True)
    title  = Column(String, nullable=False)
    author = Column(String, nullable=False)
    finished = Column(Boolean, default=False)