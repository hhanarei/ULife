from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .db_connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    h3_index = Column(String)

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    student_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    message = Column(String)
    user_id = Column(Integer)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
