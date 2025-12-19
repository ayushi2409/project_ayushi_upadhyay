from sqlalchemy import Column, Integer, String
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    designation = Column(String)
    image = Column(String)


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    mobile = Column(String)
    city = Column(String)


class Newsletter(Base):
    __tablename__ = "newsletter"

    id = Column(Integer, primary_key=True)
    email = Column(String)
