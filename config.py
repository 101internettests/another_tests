from dotenv import load_dotenv
import os
import telebot


load_dotenv()


bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))


