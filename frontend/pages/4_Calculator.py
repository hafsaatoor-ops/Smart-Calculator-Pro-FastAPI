import streamlit as st

from utils.auth import require_login
from services.api import calculate

require_login()

st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="wide"
)

st.title("🧮 Smart Calculator")

operations = {
    "Addition": "add",
    "Subtraction": "sub",
    "Multiplication": "mul",
    "Division": "div",
    "Power": "power",
    "Modulus": "mod",
    "Percentage": "percent",
    "Square Root": "sqrt"
}

selected = st.selectbox(
    "Operation",
    list(operations.keys())
)

number1 = st.number_input(
    "First Number",
    value=0.0
)

number2 = None

if operations[selected] != "sqrt":

    number2 = st.number_input(
        "Second Number",
        value=0.0
    )

if st.button("Calculate"):

    with st.spinner("Calculating..."):

        response = calculate(
            operations[selected],
            number1,
            number2
        )

    if response.status_code == 200:

        result = response.json()

        st.success("Calculation Successful ✅")
        st.balloons()

        st.metric(
            "Result",
            result["result"]
        )

    else:

        try:

            st.error(
                response.json()["detail"]
            )

        except Exception:

            st.error("Calculation failed.")