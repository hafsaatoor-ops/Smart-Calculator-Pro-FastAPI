import streamlit as st
from services.api import login, profile
from utils.session import login_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# Agar pehle se login hai to message dikhao
if st.session_state.get("logged_in"):
    st.success("✅ You are already logged in.")
    st.stop()

st.title("🧮 Smart Calculator Pro")
st.subheader("🔐 Login")

st.write("Please login to continue.")

with st.form("login_form"):

    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    submit = st.form_submit_button("Login")

if submit:

    if not email or not password:
        st.error("Please fill all fields.")

    else:

        with st.spinner("Logging in..."):

            response = login(email, password)

        if response.status_code == 200:

            profile_response = profile()

            if profile_response.status_code == 200:

                user = profile_response.json()

                login_user(
                    st.session_state.token,
                    user
                )

                st.success("Login Successful 🎉")

                st.balloons()

                st.switch_page(
                    "pages/3_Dashboard.py"
                )

            else:

                st.error("Profile loading failed.")

        else:

            try:
                st.error(
                    response.json()["detail"]
                )

            except Exception:
                st.error("Login failed.")