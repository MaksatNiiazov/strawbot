from telebot import TeleBot
from bot.keyboards import get_equipment_info_keyboard, get_main_menu_keyboard, get_done_keyboard
from texts.model_texts import MODEL_TEXT, MODEL_ORDER_WEBCAM, MODEL_EQUIPMENT
from bot.states import set_user_state

def register_model_handlers(bot: TeleBot):
    @bot.message_handler(func=lambda message: message.text == "Стать моделью")
    def model_choice(message):
        bot.send_message(message.chat.id, MODEL_TEXT)
        bot.send_message(message.chat.id, MODEL_ORDER_WEBCAM)
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=get_equipment_info_keyboard())

    @bot.message_handler(func=lambda message: message.text == "Узнать об оборудовании")
    def equipment_info(message):
        bot.send_message(message.chat.id, MODEL_EQUIPMENT)
        ask_for_portfolio(message)

    def ask_for_portfolio(message):
        markup = get_equipment_info_keyboard()
        markup.add("Главное меню")
        bot.send_message(message.chat.id, "Готовы отправить ваше портфолио?", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Отправить портфолио")
    def request_portfolio(message):
        set_user_state(message.chat.id, 'waiting_for_portfolio')
        bot.send_message(message.chat.id, "Пожалуйста, отправьте ваши фото или видео для портфолио. Нажмите 'Готово', когда закончите.", reply_markup=get_done_keyboard())