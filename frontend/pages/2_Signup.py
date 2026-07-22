import streamlit as st

from services.api import signup

st.set_page_config(
    page_title="Signup",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Create a New Account")

st.markdown(
    "Create your Smart Calculator Pro account to securely save your calculations."
)

st.divider()

with st.form("signup_form"):

    full_name = st.text_input(
        "👤 Full Name"
    )

    email = st.text_input(
        "📧 Email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    submit = st.form_submit_button(
        "📝 Create Account"
    )

if submit:

    if not full_name or not email or not password:

        st.warning(
            "Please fill all fields."
        )

    else:

        response = signup(
            full_name,
            email,
            password
        )

        if response.status_code == 200:

            st.success(
                "🎉 Account created successfully!"
            )

            st.balloons()

            st.info(
                "Now go to the Login page and sign in."
            )

        elif response.status_code == 400:

            st.error(
                response.json()["detail"]
            )

        else:

            st.error(
                "Signup failed. Please try again."
            )

st.divider()

st.caption("Already have an account? Open the Login page from the sidebar.")