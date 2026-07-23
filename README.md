# 🧮 Smart Calculator Pro

> **Enterprise Calculator Application built with FastAPI & Streamlit**

A modern full-stack calculator application featuring secure authentication, calculation history, statistics dashboard, CSV export, and an intuitive Streamlit user interface.

---

## 🚀 Features

- 🔐 User Authentication (JWT)
- 👤 User Signup & Login
- 🧮 Smart Calculator
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 📐 Modulus
- 🔢 Power
- √ Square Root
- 📊 Percentage
- 📜 Calculation History
- 🔍 Search History
- 🗑 Delete History
- 📊 Statistics Dashboard
- 📥 Export History to CSV
- 👤 User Profile
- ⚙️ Settings Page
- 🎈 Balloons on Successful Calculation
- 📱 Responsive Streamlit Interface
- 📄 Interactive Swagger API Documentation

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic

## Frontend

- Streamlit

## Other Libraries

- Requests
- Uvicorn
- Passlib
- Python-Jose

---

# 📁 Project Structure

```text
SMART_CALCULATOR_PRO/
│
├── .venv/
├── .vscode/
│
└── smart_calculator/
    │
    ├── app/
    │   │
    │   ├── __init__.py
    │   ├── main.py
    │   │
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── config.py
    │   │   ├── dependencies.py
    │   │   ├── exceptions.py
    │   │   └── security.py
    │   │
    │   ├── crud/
    │   │   ├── calculator_crud.py
    │   │   ├── history_crud.py
    │   │   ├── statistics_crud.py
    │   │   └── user_crud.py
    │   │
    │   ├── database/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── connection.py
    │   │   └── session.py
    │   │
    │   ├── middleware/
    │   │   ├── __init__.py
    │   │   └── logging_middleware.py
    │   │
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── history.py
    │   │   └── user.py
    │   │
    │   ├── routers/
    │   │   ├── __init__.py
    │   │   ├── auth_router.py
    │   │   ├── calculator_router.py
    │   │   ├── export_router.py
    │   │   ├── history_router.py
    │   │   ├── profile_router.py
    │   │   └── statistics_router.py
    │   │
    │   ├── schemas/
    │   │   ├── __init__.py
    │   │   ├── calculator_schema.py
    │   │   ├── history_schema.py
    │   │   ├── token_schema.py
    │   │   └── user_schema.py
    │   │
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── calculator_service.py
    │   │   └── statistics_services.py
    │   │
    │   ├── static/
    │   │   ├── favicon.ico
    │   │   └── logo.png
    │   │
    │   └── utils/
    │       ├── __init__.py
    │       ├── export.py
    │       ├── helper.py
    │       └── logger.py
    │
    ├── frontend/
    │   ├── __init__.py
    │   ├── streamlit_app.py
    │   ├── assets/
    │   │   ├── avatar.png
    │   │   ├── background.png
    │   │   └── logo.png
    │   ├── components/
    │   ├── pages/
    │   ├── services/
    │   │   ├── __init__.py
    │   │   └── api.py
    │   ├── styles/
    │   │   └── style.css
    │   └── utils/
    │       ├── __init__.py
    │       ├── auth.py
    │       └── session.py
    │
    ├── docs/
    │   ├── API.md
    │   ├── ARCHITECTURE.md
    │   └── DATABASE.md
    │
    ├── logs/
    │   ├── app.log
    │   └── error.log
    │
    ├── screenshots/
    │  
    │
    ├── tests/
    │   ├── test_auth.py
    │   ├── test_calculator.py
    │   ├── test_history.py
    │   └── test_statistics.py
    │
    ├── .env
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── calculator.db
    └── requirements.txt
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/hafsaatoor-ops/Smart-Calculator-Pro-FastAPI.git
```

```bash
cd smart-calculator-pro
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Docs

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 📊 API Modules

- Authentication
- Calculator
- History
- Statistics
- Export
- Profile
- Health Check

---

# 📸 Application Screenshots

This project includes **21 screenshots** showcasing both the **Backend APIs** and the **Frontend User Interface**.

The screenshots demonstrate:

- 🔐 User Authentication (Signup & Login)
- 🧮 Calculator Operations
- 📊 Statistics Dashboard
- 📜 Calculation History
- 📥 CSV Export
- 👤 User Profile
- ⚙️ Settings
- 📄 Swagger API Documentation
- 💻 Streamlit Frontend Pages
- 🚀 Backend API Responses

All screenshots are available inside the **screenshots/** folder.
> 📷 The screenshots folder contains the complete visual walkthrough of the application, including both backend API testing and frontend interface.

---

# 📂 Documentation

Project documentation is available in the **docs** folder.

- API.md
- ARCHITECTURE.md
- DATABASE.md

---

# 🧪 Testing

Test files are available inside the **tests** folder.

- Authentication Tests
- Calculator Tests
- History Tests
- Statistics Tests

---

# 🔒 Authentication

The application uses **JWT (JSON Web Token)** authentication.

Protected routes require a valid access token.

---

# 📈 Future Improvements

- PostgreSQL Support
- Docker Deployment
- Email Verification
- Password Reset
- Dark Theme
- Charts & Graphs
- Admin Dashboard
- Cloud Deployment

---

# 👩‍💻 Author

**Hafsa Toor**

BS Computer Science

The Islamia University of Bahawalpur

---

# 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.