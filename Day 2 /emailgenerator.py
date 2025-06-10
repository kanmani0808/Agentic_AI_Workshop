import streamlit as st
from google.generativeai import GenerativeModel, configure
from fpdf import FPDF
import tempfile
import os

# ---------- SETUP GEMINI API KEY ----------
GEMINI_API_KEY = "AIzaSyCuA5PVhod4jLcKExBfgIXwsV00z8rzxCk"  # replace with your actual Gemini API key
configure(api_key=GEMINI_API_KEY)
model = GenerativeModel("gemini-2.0-flash")

# ---------- STREAMLIT UI SETUP ----------
st.title("📧 AI Email Generator with Gemini")
st.markdown("""
Enter your message and choose a format and tone. The AI will generate a professional email for you.
""")

# User Input
user_text = st.text_area("✏️ Enter the text or context for the email:", height=150)

# Format and Tone Selection
format_option = st.selectbox("📂 Choose Email Format:", ["Formal", "Informal", "Apology", "Follow-up", "Thank you", "Request"])
tone_option = st.radio("🎯 Select Tone:", ["Professional", "Friendly", "Assertive", "Polite"])

# Placeholder for generated email
generated_email = ""

# Generate Button
if st.button("🔍 Generate Email"):
    if user_text:
        prompt = f"""
        Generate an {format_option.lower()} email with a {tone_option.lower()} tone.
        Context: {user_text}
        Format the email with proper greetings, body, and closing.
        """
        response = model.generate_content(prompt)
        generated_email = response.text
        st.success("✅ Email generated successfully!")
        st.text_area("📩 Generated Email:", generated_email, height=300)
    else:
        st.warning("⚠️ Please enter some text to generate an email.")

# Regenerate Button
if st.button("🔁 Regenerate Email") and user_text:
    prompt = f"""
    Regenerate an {format_option.lower()} email with a {tone_option.lower()} tone.
    Context: {user_text}
    Format the email with proper structure.
    """
    response = model.generate_content(prompt)
    generated_email = response.text
    st.text_area("📩 Regenerated Email:", generated_email, height=300)

# Download as PDF
if generated_email:
    if st.button("📥 Download Email as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in generated_email.split('\n'):
            pdf.multi_cell(0, 10, line)

        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdf.output(tmp_file.name)
            st.download_button(
                label="Download PDF",
                data=open(tmp_file.name, "rb").read(),
                file_name="generated_email.pdf",
                mime="application/pdf"
            )
        os.remove(tmp_file.name)

# Notes for User
st.markdown("""
---
⚙️ **Tips**:
- Adjust tone and format for different styles.
- Use regenerate if the first draft isn't perfect.
""")
