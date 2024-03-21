from dotenv import load_dotenv
import os
import telebot


load_dotenv()

num_1 = (os.getenv('NUM1'))

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))
