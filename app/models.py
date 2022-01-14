from re import T
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import Null, text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('NOW()'), nullable=False)
    owner_id = Column(Integer,ForeignKey('users.id',ondelete="CASCADE"),nullable=False)
    owner = relationship('User')
    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String,nullable=False)    
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('NOW()'), nullable=False)
    
    
class Vote(Base):
    __tablename__ = 'votes'
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    
    
    