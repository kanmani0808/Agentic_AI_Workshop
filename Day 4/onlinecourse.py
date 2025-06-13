import streamlit as st

# ✅ Page setup
st.set_page_config(page_title="SNS AI Course Form", page_icon="🌈", layout="centered")

# ✅ Display a rainbow-style logo and heading
st.image("https://cdn-icons-png.flaticon.com/512/1182/1182721.png", width=120)
st.markdown("<h2 style='text-align: center; color: #6A0DAD;'>SNS Institutions - Innovation Hub</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FF69B4;'>AI Learner Registration Form 🌟</h3>", unsafe_allow_html=True)
st.markdown("---")

# ✅ Form input fields
with st.form("learner_form"):
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email")
    phone = st.text_input("📱 Phone Number")
    topic = st.selectbox("💡 Interested Topic", ["Agentic AI", "Generative AI", "Prompt Engineering", "AI in Automation", "Other"])
    career = st.radio("🎓 Career", ["Student", "Technical Professional"])
    age = st.slider("🎂 Age", 15, 65, 20)
    gender = st.radio("⚧ Gender", ["Male", "Female", "Other"])

    submitted = st.form_submit_button("Submit")

import requests

if submitted:
    st.success(f"✅ Thank you, {name}! Your details have been recorded successfully.")
    
    # 👇 Add this block to send to n8n webhook
    webhook_url = "https://kanmani0808.app.n8n.cloud/webhook-test/AI- learner"
  # Replace with your test URL from n8n

    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "topic": topic,
        "career": career,
        "age": age,
        "gender": gender
    }

    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            st.info("✅ Learner data sent to n8n webhook.")
        else:
            st.warning("⚠️ Failed to send to n8n. Please check the webhook.")
    except Exception as e:
        st.error(f"❌ Error sending to n8n: {e}")

    