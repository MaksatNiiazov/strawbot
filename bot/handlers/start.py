from telebot import TeleBot
from bot.keyboards import get_main_menu_keyboard
from texts.basic import START_TEXT

def register_start_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, START_TEXT)
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=get_main_menu_keyboard())

    @bot.message_handler(func=lambda message: message.text == "Главное меню")
    def main_menu(message):
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=get_main_menu_keyboard())