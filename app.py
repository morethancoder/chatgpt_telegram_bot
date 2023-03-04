import os
import pyrogram.filters as filters
from pyrogram import Client
from modules.api import get_reply
from dotenv import load_dotenv

load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Client(name='chatgpt',api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

@bot.on_message(filters.command('start'))
def on_start(client,message):
    chat_id = message.chat.id
    text = 'hello im a bot programmed with openai gpt3.5 turbo api, how can i help you ?'
    client.send_message(chat_id,text)
    return

@bot.on_message()
def chatgpt(client,message):
    chat_id = message.chat.id
    prompt = message.text[:50]
    wait_message = client.send_message(chat_id,'⏳')
    reply = get_reply(prompt)
    client.delete_messages(chat_id,wait_message.id)
    client.send_message(chat_id,reply)
    return 

bot.run()