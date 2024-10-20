import asyncio
import requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для получения ответа "да" или "нет"
def get_yes_no_answer():
    url = "https://yesno.wtf/api"
    response = requests.get(url)
    return response.json()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Задай любой вопрос, и я отвечу 'да' или 'нет'.")

@dp.message()
async def send_yes_no_answer(message: Message):
    answer_data = get_yes_no_answer()
    answer = answer_data['answer'].capitalize()
    image_url = answer_data['image']

    # Используем send_animation для отправки GIF
    await message.answer_animation(animation=image_url, caption=answer)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())