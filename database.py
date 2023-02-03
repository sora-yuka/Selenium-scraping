from sqlalchemy import ForeignKey, ForeignKey, ForeignKey, create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class ScrapData(Base):
    """Форма создания таблицы в базе данных."""
    __tablename__ = "title"
    
    id = Column("id", Integer, primary_key=True)
    title = Column("title", String)
    
    def __init__(self, title):
        self.title = title
        
    def __repr__(self):
        return f"{self.title}"
    
    
class AdditionalData(Base):
    """Форма для создания таблицы в базе данных."""
    __tablename__ = "chapter"
    
    id = Column("id", Integer, primary_key=True)
    chapter = Column("chapter", String)
    title = Column(Integer, ForeignKey("title.id"))
    
    def __init__(self, chapter, title):
        self.chapter = chapter
        self.title = title
    
    def __repr__(self):
        return f"{self.chapter}"

engine = create_engine("sqlite:///scrap_data.db", echo=True)
Base.metadata.create_all(bind=engine)
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
"""Подключение к локальной базе данных и создание таблицю"""


"""Если вы пользуетесь существующей базой данных, то подключите ее следующим обрахом."""
# engine = create_engine("postgresql+psycopg2://user:password@localhost/database", echo=True)

Session = sessionmaker(bind=engine)
session = Session()