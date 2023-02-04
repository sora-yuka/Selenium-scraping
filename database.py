from sqlalchemy import ForeignKey, ForeignKey, ForeignKey, create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Base = declarative_base()


class EnnouncementsData(Base):
    """ Форма создания таблицы в базе данных. """
    __tablename__ = "ennouncements"
    
    id = Column("id", Integer, primary_key=True)
    ennouncement = Column("ennouncement", String)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    
    def __init__(self, ennouncement):
        self.ennouncement = ennouncement
        
    def __repr__(self):
        return f"{self.ennouncement}"
    

class EnnouncementPrices(Base):
    """ Форма для создания таблицы в базе данных. """
    __tablename__ = "prices"
    
    id = Column("id", Integer, primary_key=True)
    price = Column("price", String)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    
    def __init__(self, price):
        self.price = price
        
    def __repr__(self):
        return f"{self.price}"


class EnnouncementPosts(Base):
    """ Форма для создания таблицы в базе данных. """
    __tablename__ = "posts"
    
    id = Column("id", Integer, primary_key=True)
    date_posted = Column("post", String)
    created_time = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, date_posted):
        self.date_posted = date_posted
    
    def __repr__(self):
        return f"{self.date_posted}"
    

class EnnouncementPictures(Base):
    """ Форма для создания таблицы в базе данных. """
    __tablename__ = "pictures"
    
    id = Column("id", Integer, primary_key=True)
    picture = Column("picture", String)
    created_time = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, picture):
        self.picture = picture
    
    def __repr__(self):
        return f"{self.picture}"
    
    
engine = create_engine("sqlite:///scrap_data.db", echo=True)
Base.metadata.create_all(bind=engine)
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
""" Подключение к локальной базе данных и создание таблиц. """


""" Если вы пользуетесь существующей базой данных, то подключите ее следующим образом. """
# engine = create_engine("postgresql+psycopg2://user:password@localhost/database", echo=True)

Session = sessionmaker(bind=engine)
session = Session()