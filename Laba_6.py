import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
import asyncio

API_TOKEN = '7488910208:AAHcr_XiiKxQrhSO4wssk6W-E3-M-Y4Zf7A'  # Замените на свой токен

# Настроим логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

# В aiogram 3.x создаем Router отдельно
router = Router()

# Создаем диспетчер
dp = Dispatcher()

# Ссылка на ваше веб-приложение
web_app = WebAppInfo(url="https://github.com/Aleksandra090420/game_update")

# Создаем клавиатуру с кнопкой для WebApp
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить обновления", web_app=web_app)]
    ],
    resize_keyboard=True
)

DISC = {
    "1": "2024-11-27: Исправления ошибок и улучшения производительности.",
    "2": "2024-11-26: Добавлен новый герой и изменения на картах.",
    "3": "2024-11-25: Изменения баланса оружия.",
    "4": "2024-11-22: Добавлены новые обои и исправления ошибок.",
    "5": "2024-11-20: Улучшения геймплея и исправления ошибок.",
    "6": "2024-11-18: Новый игровой режим и изменения баланса.",
    "7": "2024-11-27: Сезонное событие и введение нового персонажа.",
    "8": "2024-11-26: Добавлены новые транспортные средства и миссии.",
    "9": "2024-11-24: Исправления ошибок и новые функции для многопользовательского режима.",
    "10": "2024-11-27: Введены новые танки и самолеты."
}

# Обработчик WebApp Data
async def buy_process(web_app_message: types.Message):
    await bot.send_message(web_app_message.chat.id, DISC.get(web_app_message.web_app_data))

# Регистрируем обработчик для типа данных WebApp с фильтром ContentType.WEB_APP_DATA
@router.message(lambda message: message.web_app_data)
async def handle_web_app_data(message: types.Message):
    # Обрабатываем данные, полученные от WebApp
    await buy_process(message)

# Запускаем бота с использованием asyncio
async def on_start():
    # Связываем Router с Dispatcher
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(on_start())