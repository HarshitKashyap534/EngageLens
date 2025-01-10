import requests
from dotenv import load_dotenv
import os
import streamlit as st


load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "eb97ae71-c3f3-4e02-8cd3-b69376c41aec"
FLOW_ID = "a14c5155-1a03-471e-910c-6afcb278b560"
APPLICATION_TOKEN = st.secrets["APP_TOKEN"]
ENDPOINT = "analysis" # The endpoint name of the flow

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("EngageLens 🔎")

    message = st.text_area("Made By Team Gryffindor", placeholder="Ask EngageLens Analytical Questions For Your Social Media Profile")

    if st.button("Run EngageLens"):
        if not message.strip():
            st.error("Please enter a message")
            return

        try:
            with st.spinner("🔄 Hang tight! We're fetching your analytics... 🚀"):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
