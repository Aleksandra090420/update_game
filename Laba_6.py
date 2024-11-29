from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Ваш токен бота
bot = Bot(token="7488910208:AAHcr_XiiKxQrhSO4wssk6W-E3-M-Y4Zf7A")
dp = Dispatcher(bot)

# Ссылка на WebApp (путь к HTML странице)
web_app = WebAppInfo(url="https://YOUR_GITHUB_PAGES_URL/game_update.html")

# Создаем клавиатуру с кнопкой для WebApp
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить обновления", web_app=web_app)]
    ],
    resize_keyboard=True
)

# Словарь с обновлениями для разных игр
DISC = {
    "1": "Обновления для Counter-Strike 2: Исправления ошибок и улучшения производительности.",
    "2": "Обновления для Dota 2: Добавлен новый герой и изменения на картах.",
    "3": "Обновления для PUBG: Изменения баланса оружия.",
    "4": "Обновления для Wallpaper Engine: Новый набор тем.",
    "5": "Обновления для Wukong: Улучшена анимация и баланс персонажей.",
    "6": "Обновления для Naraka: Bladepoint: Новые карты и персонажи.",
    "7": "Обновления для Apex Legends: Сезонные события и изменения баланса.",
    "8": "Обновления для GTA V: Новые миссии и исправления.",
    "9": "Обновления для Deadlock: Исправления ошибок и новый контент.",
    "10": "Обновления для War Thunder: Новые танки и самолеты."
}

# Отправляем клавиатуру пользователю при старте
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Нажмите кнопку ниже, чтобы получить обновления игр.", reply_markup=keyboard)

# Обработка данных, полученных от WebApp (когда пользователь нажимает кнопку в WebApp)
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def buy_process(web_app_message):
    game_id = web_app_message.web_app_data  # Получаем ID игры, который был отправлен из WebApp
    update_info = DISC.get(game_id, "Информация не найдена.")
    await bot.send_message(web_app_message.chat.id, update_info)  # Отправляем информацию обратно в чат

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)