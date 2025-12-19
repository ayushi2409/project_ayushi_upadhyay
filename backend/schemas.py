from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str
    image: str


class ClientCreate(BaseModel):
    name: str
    description: str
    designation: str
    image: str


class ContactCreate(BaseModel):
    full_name: str
    email: str
    mobile: str
    city: str


class NewsletterCreate(BaseModel):
    email: str
