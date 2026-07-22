import streamlit as st

from components.sidebar import show_sidebar
from utils import initialize_session

st.set_page_config(
    page_title="Smart Calculator Pro",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_session()
show_sidebar()

st.markdown("""
<style>

.main{
    background:#f5f7fa;
}

h1{
    color:#0066FF;
    text-align:center;
}

div[data-testid="stSidebar"]{
    background:#1E293B;
}

div[data-testid="stSidebar"] *{
    color:white;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    background:#0066FF;
    color:white;
    border:none;
    height:45px;
    font-size:16px;
}

.stButton>button:hover{
    background:#0052CC;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

st.title("🧮 Smart Calculator Pro")

st.subheader("Enterprise Edition")

st.success("Welcome to Smart Calculator Pro 🎉")

st.markdown("""
## 👋 Welcome

A modern calculator application built with:

- ⚡ FastAPI
- 🎨 Streamlit
- 🔐 JWT Authentication
- 🗄️ SQLAlchemy
- 💾 SQLite
- 📊 Statistics Dashboard
- 📜 Calculation History
- 📥 CSV Export

---

## ✨ Features

✅ Secure Login & Signup

✅ Calculator with Multiple Operations

✅ User Profile

✅ History with Search & Delete

✅ Statistics Dashboard

✅ CSV Export

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic

---

## 🚀 Getting Started

Use the **sidebar** to:

- 🔐 Login
- 📝 Signup
- 🧮 Calculator
- 📜 History
- 📊 Dashboard
- 👤 Profile
- ⚙️ Settings

Enjoy using **Smart Calculator Pro**!
""")

st.success("Project Completed Successfully 🎉")

st.markdown("""
<div class="footer">

Made with ❤️ by Hafsa Toor using FastAPI + Streamlit

</div>
""", unsafe_allow_html=True)