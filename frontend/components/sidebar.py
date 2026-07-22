import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.markdown("# 🧮 Smart Calculator Pro")

        st.caption("Enterprise Edition")

        st.divider()

        st.success("Backend Connected ✅")

        st.divider()

        st.markdown("### Navigation")

        st.page_link(
            "streamlit_app.py",
            label="🏠 Home"
        )

        st.page_link(
            "pages/1_Login.py",
            label="🔐 Login"
        )

        st.page_link(
            "pages/2_Signup.py",
            label="📝 Signup"
        )

        st.page_link(
            "pages/3_Dashboard.py",
            label="📊 Dashboard"
        )

        st.page_link(
            "pages/4_Calculator.py",
            label="🧮 Calculator"
        )

        st.page_link(
            "pages/5_History.py",
            label="📜 History"
        )

        st.page_link(
            "pages/6_Profile.py",
            label="👤 Profile"
        )

        st.page_link(
            "pages/7_Settings.py",
            label="⚙️ Settings"
        )

        st.divider()

        st.info("Version 1.0.0")