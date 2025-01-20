from fastapi import FastAPI
from threading import Thread
from bot import create_bot

app = FastAPI()

def run_telegram_bot():
    bot = create_bot()
    bot.polling(none_stop=True)

@app.get("/")
async def read_root():
    return {"message": "FastAPI is running alongside the Telegram bot!"}

if __name__ == "__main__":
    # Запуск бота в отдельном потоке
    bot_thread = Thread(target=run_telegram_bot)
    bot_thread.start()

    # Запуск FastAPI приложения
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
