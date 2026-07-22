# Smart Calculator Pro Architecture

## Overview

Smart Calculator Pro is a full-stack web application developed using FastAPI and Streamlit.

The application follows a layered architecture to keep the project modular, maintainable, and scalable.

---

# Architecture Diagram

```
                 User
                   │
                   ▼
          Streamlit Frontend
                   │
          HTTP Requests (REST API)
                   │
                   ▼
             FastAPI Backend
                   │
     ┌─────────────┼─────────────┐
     │             │             │
     ▼             ▼             ▼
  Routers       Services       CRUD
     │             │             │
     └─────────────┼─────────────┘
                   ▼
              SQLAlchemy ORM
                   │
                   ▼
               SQLite Database
```

---

# Components

## Frontend

Built using Streamlit.

Responsibilities:

- User Interface
- Authentication
- Calculator
- Dashboard
- History
- Profile
- Settings

---

## Backend

Built using FastAPI.

Responsibilities:

- Business Logic
- JWT Authentication
- Validation
- Database Operations
- API Endpoints

---

## Database

SQLite is used as the database.

Stores:

- Users
- Calculation History

---

## Authentication

JWT Token Authentication protects all secure endpoints.

---

## Logging

Application logs are stored in:

```
logs/app.log
```

Errors can be stored in:

```
logs/error.log
```

---

## API Communication

The frontend communicates with the backend using REST APIs.

---

# Project Layers

Presentation Layer

↓

Business Layer

↓

CRUD Layer

↓

Database Layer

---

# Technologies Used

- FastAPI
- Streamlit
- SQLAlchemy
- SQLite
- JWT
- Python