from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal
from models import Base, Project, Client, Contact, Newsletter
from schemas import *


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (safe for assignment)
    allow_credentials=True,
    allow_methods=["*"],   # allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- PROJECT APIs ----------------

@app.get("/")
def home():
    return {"message": "Flipr Backend Running"}

@app.post("/admin/project")
def add_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(
        name=project.name,
        description=project.description,
        image=project.image
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return {"message": "Project added successfully", "project": new_project}

# Get All Projects (Landing Page)
@app.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


# ---------------- CLIENT APIs ----------------

# Add Client (Admin)
@app.post("/admin/client")
def add_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = Client(
        name=client.name,
        description=client.description,
        designation=client.designation,
        image=client.image
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return {"message": "Client added successfully", "client": new_client}


# Get All Clients (Landing Page)
@app.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()


# ---------------- CONTACT FORM APIs ----------------

# Submit Contact Form (User)
@app.post("/contact")
def submit_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    new_contact = Contact(
        full_name=contact.full_name,
        email=contact.email,
        mobile=contact.mobile,
        city=contact.city
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"message": "Contact form submitted successfully"}


# View Contact Responses (Admin)
@app.get("/admin/contacts")
def view_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()


# ---------------- NEWSLETTER APIs ----------------

# Subscribe Newsletter (User)
@app.post("/newsletter")
def subscribe_newsletter(newsletter: NewsletterCreate, db: Session = Depends(get_db)):
    new_sub = Newsletter(email=newsletter.email)
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return {"message": "Subscribed to newsletter successfully"}


# View Subscribed Emails (Admin)
@app.get("/admin/newsletter")
def view_newsletter(db: Session = Depends(get_db)):
    return db.query(Newsletter).all()
