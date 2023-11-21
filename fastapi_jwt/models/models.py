from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON
from sqlalchemy.orm import declarative_base
from datetime import datetime


Base=declarative_base()
metadata = MetaData()

class Roles(Base):
    _tablename_ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=False)


class Users(Base):
    _tablename_ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=("now()"))
    role_id = complex(Integer, ForeignKey("roles.id", ondelete="CASCADE"))


