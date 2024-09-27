from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Стать моделью"))
    markup.row(KeyboardButton("О платформе"), KeyboardButton("Политика конфиденциальности"))
    return markup

def get_equipment_info_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Узнать об оборудовании"), KeyboardButton("Отправить портфолио"))
    markup.row(KeyboardButton("Пройти опрос"))
    markup.row(KeyboardButton("Главное меню"))
    return markup

def get_yes_no_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Да"), KeyboardButton("Нет"))
    return markup

def get_done_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Готово"))
    return markup