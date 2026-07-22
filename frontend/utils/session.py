import streamlit as st


def initialize_session():

    defaults = {

        "logged_in": False,

        "token": None,

        "user": None

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


def login_user(token, user):

    st.session_state.logged_in = True

    st.session_state.token = token

    st.session_state.user = user


def logout_user():

    st.session_state.logged_in = False

    st.session_state.token = None

    st.session_state.user = None