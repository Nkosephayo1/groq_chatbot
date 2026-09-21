import streamlit as st
import requests

from config import GROQ_API_KEY, GROQ_MODEL


st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖"
)

st.title("Chatbot with Groq AI")


# -----------------------------
# API KEY STATUS
# -----------------------------

if GROQ_API_KEY:
    st.success("Groq API key loaded successfully.")
else:
    st.error("❗ GROQ_API_KEY is missing! Check your configuration.")


st.write(f"Default model: `{GROQ_MODEL}`")


# -----------------------------
# USER INPUT
# -----------------------------

user_input = st.text_area(
    "Enter your question or prompt:",
    height=150
)


# -----------------------------
# GENERATE RESPONSE
# -----------------------------

if st.button("Generate Response"):

    if not user_input.strip():
        st.warning("Please enter a prompt first.")

    elif not GROQ_API_KEY:
        st.error("Cannot generate a response without a Groq API key.")

    else:

        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "max_tokens": 2000
        }

        try:

            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=60
            )

            # Show the actual Groq error message
            if response.status_code != 200:

                st.error(
                    f"Groq API returned status code: "
                    f"{response.status_code}"
                )

                st.code(response.text)

            else:

                data = response.json()

                answer = data["choices"][0]["message"]["content"]

                st.markdown("### Response")

                st.write(answer)

        except requests.exceptions.RequestException as e:

            st.error(f"Request error: {e}")

        except KeyError:

            st.error("Unexpected response format from Groq.")

            st.json(data)
