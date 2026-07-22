import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


# ==========================
# Token Management
# ==========================

def set_token(access_token: str):
    st.session_state["token"] = access_token


def get_headers():

    token = st.session_state.get("token")

    if token:
        return {
            "Authorization": f"Bearer {token}"
        }

    return {}


# ==========================
# Authentication
# ==========================

def signup(full_name, email, password):

    response = requests.post(
        f"{BASE_URL}/auth/signup",
        json={
            "full_name": full_name,
            "email": email,
            "password": password
        }
    )

    return response


def login(email, password):

    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    if response.status_code == 200:

        access_token = response.json()["access_token"]

        set_token(access_token)

    return response


def profile():

    response = requests.get(
        f"{BASE_URL}/auth/profile",
        headers=get_headers()
    )

    return response


# ==========================
# Calculator
# ==========================

def calculate(operation, number1, number2=None):

    payload = {
        "operation": operation,
        "number1": number1,
        "number2": number2
    }

    response = requests.post(
        f"{BASE_URL}/calculator/calculate",
        json=payload,
        headers=get_headers()
    )

    return response


# ==========================
# History
# ==========================

def get_history(page=1, limit=10, search=""):

    response = requests.get(
        f"{BASE_URL}/history/",
        params={
            "page": page,
            "limit": limit,
            "search": search
        },
        headers=get_headers()
    )

    return response


def delete_history(history_id):

    response = requests.delete(
        f"{BASE_URL}/history/{history_id}",
        headers=get_headers()
    )

    return response


# ==========================
# Statistics
# ==========================

def statistics():

    response = requests.get(
        f"{BASE_URL}/statistics",
        headers=get_headers()
    )

    return response


# ==========================
# CSV Export
# ==========================

def export_csv():

    response = requests.get(
        f"{BASE_URL}/export",
        headers=get_headers()
    )

    return response