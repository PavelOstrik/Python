import os
from aiogram import *
from pytube import *
from config import *

# name_bot = Video_Download_Youtube_Bot
bot = Bot(Token)
dp = Dispatcher(bot)
#  Dispatcher принимает все апдейты и обрабатывает их.

# Начинаем наш диалог
# Обработчик сообщений
@dp.message_handler(commands=['start'])
async def start_mesage(message:types.Message):
    chat_id = message.chat.id  # идентификатор чата
# Функция send_message принимает идентификатор чата (берем его из сообщения) и текст для отправки.
    await bot.send_message(chat_id, 'Привет, я могу скачивать видео с Youtube\n'
                                    'Отправь мне ссылку')

# Обработчик ссылок
@dp.message_handler()
async def text_message(message:types.Message):                                    
    chat_id = message.chat.id
    url = message.text # сюда присваивается ссылка
    yt = YouTube(url)
    
    # message.text.startswith если текст начинается с такого отрезка
    if message.text.startswith == 'https://www.youtube' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f'*Начинаю загрузку видео* : *{yt.title}*\n'
                                        f'*С канала *: [{yt.author}]({yt.channel_url})', parse_mode='Markdown')
        # yt.title название нашего видео
        # yt.author автор видео
        # yt.channel_url название канала
        # * parse_mode='Markdown' делаем шрифт жирным 

        await download_youtube_video(url, message, bot)

# Создаём функцию загрузки видео
async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    # yt.streams поток видео
    # Функция фильтрации → Только для извлечения файла с расширением в формате mp4
    
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    # get_highest_resolution() качает видео с максимальным качеством
    # download() функция загрузки
    
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
    # Создаем папку и указываем название файла    
    # rb Только для чтения (бинарный).     
        
        await bot.send_video(message.chat.id, video, caption='*Вот ваше видео*', parse_mode='Markdown') 
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}') # удалит наш ролик
        # Метод os.remove() позволит вам удалить файл, а метод os.rmdir() — пустую папку
        

# Начинаем получать сообщения и все события
if __name__ == '__main__':
    executor.start_polling(dp)




