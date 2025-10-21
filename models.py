from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from database import Base 


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(10))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())
    
    posts = relationship('Post', back_populates='users')
    
class Post(Base): 
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    
    title = Column(String(100), nullable=False)
    content = Column(String(255), unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), 
                        onupdate=func.now())
    
    users = relationship('User', back_populates='posts')
    
