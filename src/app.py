import streamlit as st

from src.logic import convert_currency, EXCHANGE_RATES


def setup_page() -> None:
    """Configure Streamlit page settings and apply RTL custom styling."""
    st.set_page_config(
        page_title="ממיר מטבעות גלובלי", page_icon="💰", layout="centered"
    )
    st.markdown(
        """
        <style>
        .stApp { direction: RTL; text-align: right; }
        div[data-baseweb="select"] { direction: RTL; }
        input { direction: LTR !important; text-align: right !important; }
        .rtl-title { text-align: right; direction: RTL; font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem; }
        .rtl-subtitle { text-align: right; direction: RTL; font-size: 1.5rem; color: #555555; margin-bottom: 2rem; }
        [data-testid="stMetric"] { display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%; }
        [data-testid="stMetricLabel"] { text-align: center; width: 100%; }
        [data-testid="stMetricValue"] { text-align: center; width: 100%; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header() -> None:
    """Render the application titles using safe HTML containers."""
    st.markdown(
        '<div class="rtl-title">💰 ממיר מטבעות גלובלי</div>', unsafe_allow_html=True
    )
    st.markdown(
        '<div class="rtl-subtitle">חישוב שערים דינמי בזמן אמת</div>',
        unsafe_allow_html=True,
    )


def render_converter() -> None:
    """Render the currency conversion form layout and handle submission logic."""
    amount = st.number_input("הכניסו סכום להמרה:", value=100.0, step=1.0)
    currencies = list(EXCHANGE_RATES.keys())

    col1, col2 = st.columns(2)
    with col1:
        from_curr = st.selectbox(
            "ממטבע:",
            currencies,
            index=currencies.index("ILS") if "ILS" in currencies else 0,
        )
    with col2:
        to_curr = st.selectbox(
            "למטבע:",
            currencies,
            index=currencies.index("USD") if "USD" in currencies else 0,
        )

    if st.button("חשב המרה ✨", use_container_width=True):
        try:
            result = convert_currency(amount, from_curr, to_curr)
            st.success(f"**תוצאת ההמרה:** {result:.2f} {to_curr}")
        except ValueError as e:
            st.error(f"❌ שגיאה: {e}")


def main() -> None:
    """Application main entry point execution flow."""
    setup_page()
    render_header()
    render_converter()


if __name__ == "__main__":
    main()
