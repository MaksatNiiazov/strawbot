from telebot import TeleBot
from bot.keyboards import get_main_menu_keyboard
from texts.basic import CONFIDENTIALITY_POLICY
from texts.model_texts import ABOUT_PLATFORM

def register_platform_handlers(bot: TeleBot):
    @bot.message_handler(func=lambda message: message.text == "О платформе")
    def about_platform_info(message):
        bot.send_message(message.chat.id, ABOUT_PLATFORM)
        bot.send_message(message.chat.id, "Если у вас есть вопросы, дайте знать!", reply_markup=get_main_menu_keyboard())

    @bot.message_handler(func=lambda message: message.text == "Политика конфиденциальности")
    def confidentiality_policy_info(message):
        bot.send_message(message.chat.id, CONFIDENTIALITY_POLICY)
        bot.send_message(message.chat.id, "Если у вас есть вопросы, дайте знать!", reply_markup=get_main_menu_keyboard())