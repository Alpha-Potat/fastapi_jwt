from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime


metadata = MetaData()

class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = "Role"

    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    name: Mapped[str]=mapped_column(String, nullable=False)
    permissions: Mapped[str]=mapped_column(JSON)


class User(Base):
    __tablename__ = "User"
    
    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    email: Mapped[str]=mapped_column(String, nullable=False)
    username: Mapped[str]=mapped_column(String, nullable=False)
    hashed_password: Mapped[str]=mapped_column(String, nullable=False)
    registered_at: Mapped[int]=mapped_column(Integer, default=datetime.utcnow)
    role_id: Mapped[int]=mapped_column(Integer, ForeignKey("Role.id", ondelete="CASCADE"))
    is_active: Mapped[bool]=mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool]=mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool]=mapped_column(Boolean, default=False, nullable=False)



