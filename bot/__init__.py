from telebot import TeleBot
from config.config import BOT_TOKEN
from bot.handlers import register_handlers

def create_bot():
    bot = TeleBot(BOT_TOKEN)
    register_handlers(bot)
    return bot