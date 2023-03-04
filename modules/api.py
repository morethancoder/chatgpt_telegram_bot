import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_reply(prompt,max_words=50):
    response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role":"user","content":prompt}],
    max_tokens=max_words
    )
    response_message = response.to_dict()['choices'][0]['message']['content']
    return response_message