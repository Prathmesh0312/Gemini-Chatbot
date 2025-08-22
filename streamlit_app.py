import streamlit as st
import requests
import os

st.set_page_config(page_title="GenAI Web Agent", layout="centered")

st.title(" GenAI Website Agent")
st.markdown("Enter a URL and your instruction for Gemini (e.g. *summarize, explain, bullet points, tweet*).")

# Input fields
url = st.text_input("🔗 Website URL", placeholder="https://en.wikipedia.org/wiki/Starbucks")
instruction = st.text_area(" Instruction", placeholder="Summarize this in bullet points", height=100)

# Submit button
if st.button(" Generate", use_container_width=True):
    if not url or not instruction:
        st.warning("Please provide both a URL and an instruction.")
    else:
        with st.spinner("Thinking... 🤔"):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/generate",
                    json={"url": url, "instruction": instruction}
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success(" Response Generated")

                    st.subheader(" Output")
                    st.markdown(data["output"])

                    st.subheader(" Moderation")
                    st.write(f"Toxicity Score: `{data['toxicity']}`")
                    st.write(f"Flagged: `{data['flagged']}`")
                    st.write(f"Run ID: `{data['run_id']}`")
                else:
                    st.error(f"❌ Error: {response.json().get('detail')}")
            except Exception as e:
                st.error(f" Request failed: {e}")
