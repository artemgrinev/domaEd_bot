from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    last_name = Column('last_name', String)
    first_name = Column('first_name', String)
    # recipes = relationship("Recipes", default='')
    registrate_date = Column('registrate_date', DateTime(), default=datetime.now)


class Recipes(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    link = Column('link', String)
    ingredients = Column('ingredients', String(1000))
    create_date = Column('create_date', DateTime(), default=datetime.now)
    update_date = Column('update_date', DateTime(), default=datetime.now, onupdate=datetime.now)


class ActionsUsers(Base):
    __tablename__ = 'actions_users'

    id = Column(Integer, primary_key=True)
    user_id = ForeignKey("users.id")
    date = Column('date', DateTime(), default=datetime.now)

