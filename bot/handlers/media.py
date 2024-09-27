from telebot import TeleBot
from config.config import ADMIN_CHAT_ID
from bot.keyboards import get_main_menu_keyboard, get_done_keyboard
from bot.states import get_user_state, clear_user_state  # Импортируем get_user_state

def register_media_handlers(bot: TeleBot):
    @bot.message_handler(func=lambda message: get_user_state(message.chat.id) == 'waiting_for_portfolio', content_types=['photo', 'video'])
    def handle_media(message):
        if message.photo:
            file_id = message.photo[-1].file_id
            bot.send_photo(ADMIN_CHAT_ID, file_id, caption=f"Новое фото от пользователя {message.from_user.id}")
        elif message.video:
            file_id = message.video.file_id
            bot.send_video(ADMIN_CHAT_ID, file_id, caption=f"Новое видео от пользователя {message.from_user.id}")
        
        bot.reply_to(message, "Спасибо за предоставленные материалы. Вы можете отправить больше медиафайлов или нажать 'Готово', когда закончите.", reply_markup=get_done_keyboard())

    @bot.message_handler(func=lambda message: message.text == "Готово")
    def done_sending_media(message):
        if get_user_state(message.chat.id) == 'waiting_for_portfolio':
            clear_user_state(message.chat.id)
            bot.send_message(message.chat.id, "Спасибо за предоставленные материалы. Наш HR-специалист рассмотрит их в ближайшее время.", reply_markup=get_main_menu_keyboard())
        else:
            bot.reply_to(message, "Извините, но сейчас не время для отправки медиафайлов. Пожалуйста, следуйте инструкциям бота.")