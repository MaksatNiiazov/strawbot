from telebot import TeleBot
from bot.keyboards import get_yes_no_keyboard, get_main_menu_keyboard
from texts.model_texts import survey_questions
from bot.states import set_user_state, get_user_state, clear_user_state

def register_survey_handlers(bot: TeleBot):
    @bot.message_handler(func=lambda message: message.text == "Пройти опрос")
    def start_survey(message):
        set_user_state(message.chat.id, 'survey_0')
        bot.send_message(message.chat.id, "Отлично! Давайте начнем опрос.")
        ask_question(bot, message, 0)

    @bot.message_handler(func=lambda message: get_user_state(message.chat.id) and get_user_state(message.chat.id).startswith('survey_'))
    def handle_survey_answer(message):
        current_question = int(get_user_state(message.chat.id).split('_')[1])
        
        # Сохраняем ответ (в реальном приложении здесь должна быть логика сохранения в базу данных)
        print(f"Ответ на вопрос {current_question + 1}: {message.text}")
        
        if current_question + 1 < len(survey_questions):
            set_user_state(message.chat.id, f'survey_{current_question + 1}')
            ask_question(bot, message, current_question + 1)
        else:
            clear_user_state(message.chat.id)
            bot.send_message(message.chat.id, "Спасибо за ваши ответы! Мы свяжемся с вами в ближайшее время.", reply_markup=get_main_menu_keyboard())

def ask_question(bot, message, question_number):
    bot.send_message(message.chat.id, survey_questions[question_number], reply_markup=get_yes_no_keyboard())