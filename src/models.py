import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'Person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer,ForeignKey("Comment.autorID"), primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey("Media.id"), primary_key=True)
    userID =Column(Integer,ForeignKey("Person.id"))

class Media(Base):
    __tablename__ = "Media"

    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    typeMedia = Column(Integer)
    url = Column(String(250))
    postID = Column (Integer)
class Comment(Base):
    __tablename__ = "Comment"

    id = Column (Integer,primary_key=True)
    comment = Column(String(250))
    autorID = Column(Integer,ForeignKey("Post.id"))
    postID = Column(Integer)
class Followers(Base):
    __tablename__ ="Followers"

    userFollowerID = Column(Integer,ForeignKey("Person.id"),primary_key=True)
    userID = Column(Integer,ForeignKey("Person.id"),primary_key=True)



    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')