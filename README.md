# Full Stack Admin Dashboard

This project is a simple full-stack web application built as part of a placement assignment.
It includes a React-based admin panel and a FastAPI backend connected to a lightweight SQLite database.

The application allows an admin to manage projects and clients, while users can submit contact details
and subscribe to a newsletter.

---

## Features

### Admin Panel (React)
- Add new projects
- Add client details
- View contact form submissions
- View newsletter subscribers

### Backend (FastAPI)
- REST APIs for projects, clients, contacts, and newsletter
- SQLite database for quick and simple setup
- CORS enabled for frontend-backend communication
- Swagger UI for API testing

---

## Tech Stack

### Frontend
- React (Vite)
- Axios
- Custom CSS

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

## Project Structure

```
flipr-assessment/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── __init__.py
│
├── admin-panel/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

## Setup Instructions

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run the backend server:

```bash
uvicorn backend.main:app --reload
```

API documentation will be available at:
```
http://127.0.0.1:8000/docs
```

---

### Admin Panel Setup

```bash
cd admin-panel
npm install
npm run dev
```

Admin panel will run at:
```
http://localhost:5173
```

---

## API Endpoints

### Projects
- POST `/admin/project`
- GET `/projects`

### Clients
- POST `/admin/client`
- GET `/clients`

### Contact Form
- POST `/contact`
- GET `/admin/contacts`

### Newsletter
- POST `/newsletter`
- GET `/admin/newsletter`

---

## Notes

- Authentication is not implemented as it was not required for the assignment
- Image fields use image URLs for simplicity
- SQLite is used for quick local testing
- Code is structured to remain simple and readable

---

## License

This project is created for educational and assessment purposes.
