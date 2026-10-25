
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

from dotenv import load_dotenv
load_dotenv(".env")

st.set_page_config(
    page_title="NoteGenius AI",
    page_icon="📚"
)

st.title("📚 NoteGenius AI")
st.subheader("Your Personal AI Study Assistant")

api_key = os.getenv("GEMINI_API_KEY")

notes = st.text_area(
    "Paste your study notes here",
    height=250,
    placeholder="Paste your notes here..."
)

if st.button("✨ Summarize Notes"):
    if not notes.strip():
        st.warning("Please paste your notes first.")
    elif not api_key:
        st.error("API key not found. Check your .env file.")
        st.write("Debug: .env file found:", os.path.exists(".env"))
    else:
        try:
            with st.spinner("AI is summarizing your notes..."):
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=(
                        "Summarize these study notes in simple "
                        "language using headings and bullet points:\n\n"
                        + notes
                    )
                )

            st.subheader("📝 Your Summary")
            st.write(response.text)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
