import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import yt_dlp

TOKEN = "7434822725:AAFUaXYs84seAvV9gOex1OBjuOuuwKVuTxk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Бот запущен! Пришли название песни.")

@dp.message()
async def get_audio(message: types.Message):
    await message.answer("Скачиваю...")
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
            'outtmpl': 'music.mp3',
            'quiet': True,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'cookiefile': 'cookies.txt',
        }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{message.text}"])
        if os.path.exists("music.mp3"):
            await message.answer_audio(audio=types.FSInputFile("music.mp3"))
            os.remove("music.mp3")
        else:
            await message.answer("Не удалось найти файл.")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
