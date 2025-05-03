import streamlit as st
import requests

st.set_page_config(page_title="Essay Writer", layout="centered")
st.title("LangGraph Essay Writer")

topic = st.text_input("Enter your essay topic:", "Pizza Shop")

if st.button("Generate Essay"):
    with st.spinner("Generating essay..."):
        try:
            res = requests.post(
                "https://essay-writer-f41700cda15f.herokuapp.com/generate_essay",
                json={"topic": topic}
            )
            if res.status_code == 200:
                output = res.json()
                for key, value in output.items():
                    st.markdown(f"**{key.capitalize()}**\n\n{value}\n")
            else:
                st.error(f"Error: {res.status_code} - {res.text}")
        except Exception as e:
            st.error(f"Exception occurred: {e}")
