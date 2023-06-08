# Main.py
import streamlit as st
from components.agent_selector import agent_selector

from components.verify_backend import verify_backend

verify_backend()

st.set_page_config(
    page_title="AGiXT",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <img src="https://josh-xt.github.io/AGiXT/images/AGiXTwhiteborder.svg" width="100%">
    """,
    unsafe_allow_html=True,
)

st.markdown("## Useful Links")
st.markdown(
    """
- [AGiXT Documentation](https://josh-xt.github.io/AGiXT/)
- [AGiXT GitHub](https://github.com/Josh-XT/AGiXT)
- [AGiXT Discord](https://discord.gg/d3TkHRZcjD)"""
)