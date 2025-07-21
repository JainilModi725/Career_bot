
import streamlit as st
import requests

st.set_page_config(page_title="Career Advisor Bot", layout="centered")

st.title("💼 AI Career & Upskilling Advisor")
st.markdown("Ask me anything about careers, resumes, or upskilling!")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

user_input = st.text_input("👨‍🎓 Your question:", placeholder="How do I write a good resume?")

if st.button("Get Advice"):
    if user_input:
        with st.spinner("Thinking..."):
            output = query({"inputs": user_input})
            if "error" in output:
                st.error(f"API Error: {output['error']} - {output['message']}")
            else:
                generated = output[0]["generated_text"] if isinstance(output, list) else output
                st.success("💬 Advice:")
                st.write(generated)
