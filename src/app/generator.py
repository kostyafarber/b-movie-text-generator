import openai
import streamlit as st

class Generator(openai.Completion):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

        openai.api_key = st.secrets['OPENAI_API_KEY']

    def generate_text(self, prompt):

        response = self.create(
                            engine="davinci-instruct-beta-v3",
                            prompt=prompt,
                            temperature=0.8,
                            max_tokens=300,
                            top_p=1,
                            frequency_penalty=0,
                            presence_penalty=0
                            )

        return response['choices'][0]['text']

