import streamlit as st
import requests

WEBHOOK_URL = "https://kanmani0808.app.n8n.cloud/webhook-test/68c1e8cb-9e7c-44c1-bde7-0e9f69d125e7"

VALID_USERS = {
    "admin": "admin123",
    "john": "john123",
}

def login_page():
    st.header("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if VALID_USERS.get(username) == password:
            st.session_state["authenticated"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials.")

def meeting_form():
    st.title("📝 Submit Meeting Action Item")
    name = st.text_input("Full Name")
    topic = st.text_input("Topic Discussed")
    task = st.text_input("Task Allocated")
    due_date = st.date_input("Due Date")
    email = st.text_input("Email")

    if st.button("Submit"):
        data = {
            "name": name,
            "topic": topic,
            "task": task,
            "due_date": str(due_date),
            "email": email,
        }
        try:
            res = requests.post(WEBHOOK_URL, json=data)
            res.raise_for_status()
            st.success("Data submitted successfully!")
            st.json(data)
        except Exception as e:
            st.error(f"Submission failed: {e}")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state["authenticated"]:
    meeting_form()
else:
    login_page()

st.caption("Built with Streamlit • © 2025")