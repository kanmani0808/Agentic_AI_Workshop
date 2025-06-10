
import streamlit as st
import random

st.set_page_config(page_title="Generative AI Course", layout="centered", page_icon="🤖")

# Custom styling
st.markdown("""
    <style>
    .main {background-color: #fdfdfd;}
    .block-container {
        padding: 2rem;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Generative AI: Quick Learning Module")

# Define simple topics and questions with multiple correct options
topics = {
    "What Can Generative AI Do?": {
        "question": "Select all that apply:",
        "options": [
            "Generate text", 
            "Create images", 
            "Build physical robots", 
            "Compose music",
            "Train a dog"
        ],
        "correct": [
            "Generate text", 
            "Create images", 
            "Compose music"
        ]
    },
    "Popular Gen AI Tools": {
        "question": "Which of the following are generative AI tools?",
        "options": [
            "ChatGPT", 
            "Stable Diffusion", 
            "Photoshop", 
            "DALL·E", 
            "Excel"
        ],
        "correct": [
            "ChatGPT", 
            "Stable Diffusion", 
            "DALL·E"
        ]
    },
    "Responsible AI Use": {
        "question": "Choose the ethical considerations of Gen AI:",
        "options": [
            "Bias and fairness", 
            "Misinformation", 
            "Faster downloads", 
            "Security threats"
        ],
        "correct": [
            "Bias and fairness", 
            "Misinformation", 
            "Security threats"
        ]
    }
}

# Topic selector with friendly names
selected_topic = st.selectbox("📘 Choose a Lesson", list(topics.keys()))

# Get topic content
content = topics[selected_topic]
st.header(f"🧠 {selected_topic}")
st.write(content["question"])

# Multi-select for multiple answer questions
selected_answers = st.multiselect("Drag & drop your answers below:", content["options"])

if st.button("Check Answers"):
    if set(selected_answers) == set(content["correct"]):
        st.success("✅ Correct!")
    else:
        st.error("❌ Some answers are incorrect or missing.")

# Capstone project upload section
st.divider()
st.header("📤 Submit Your Mini Project")
uploaded_file = st.file_uploader("Upload a demo or concept file (.py or .txt)", type=['py', 'txt'])
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
