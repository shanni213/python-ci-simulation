import streamlit as st
from src.logic import convert_currency

st.set_page_config(
    page_title="ממיר מטבעות גלובלי",
    page_icon="💰",
    layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        direction: RTL;
        text-align: right;
    }
    div[data-baseweb="select"] {
        direction: RTL;
    }
    input {
        direction: LTR !important;
        text-align: right !important;
    }
    .rtl-title {
        text-align: right;
        direction: RTL;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .rtl-subtitle {
        text-align: right;
        direction: RTL;
        font-size: 1.5rem;
        color: #555555;
        margin-bottom: 2rem;
    }
    .result-text {
        direction: LTR;
        text-align: right;
        display: inline-block;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="rtl-title">💰 ממיר מטבעות גלובלי</div>', unsafe_allow_html=True)
st.markdown('<div class="rtl-subtitle">חישוב שערים דינמי בזמן אמת</div>', unsafe_allow_html=True)

amount = st.number_input("הכניסי סכום להמרה:", value=100.0, step=1.0)
currencies = ["ILS", "USD", "EUR"]

col1, col2 = st.columns(2)
with col1:
    from_curr = st.selectbox("ממטבע:", currencies, index=0)
with col2:
    to_curr = st.selectbox("למטבע:", currencies, index=2)

if st.button("חשב המרה ✨", use_container_width=True):
    try:
        result = convert_currency(amount, from_curr, to_curr)
        st.markdown(f'<div style="text-align: center; font-size: 2rem; font-weight: bold; color: #008080;">{result:.2f} {to_curr}</div>', unsafe_allow_html=True)
    except ValueError as e:
        st.error(f"❌ שגיאה: {e}")