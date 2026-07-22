import streamlit as st

from utils.auth import require_login
from services.api import profile

require_login()

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

st.title("👤 My Profile")

response = profile()

if response.status_code == 200:

    user = response.json()

    st.success("Profile Loaded Successfully ✅")

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "👤 Full Name",
            value=user.get("full_name", ""),
            disabled=True
        )

        st.text_input(
            "📧 Email",
            value=user.get("email", ""),
            disabled=True
        )

    with col2:

        st.text_input(
            "User ID",
            value=str(user.get("🆔 id", "")),
            disabled=True
        )

        status = "Active" if user.get("is_active") else "Inactive"

        st.text_input(
            "✅ Status",
            value=status,
            disabled=True
        )

    st.text_input(
        "📅 Account Created",
        value=user.get("created_at", ""),
        disabled=True
    )

else:

    st.error("Unable to load profile.")