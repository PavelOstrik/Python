# Сюда все функции отправляющие сообщения


from aiogram import types

from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в КОНФЕТЫ!\n'
                           f'Мы по очереди берем конфеты, не более 28 шт за раз.\n'
                           f'Кто забрал последние конфеты, тот WIN...\n'
                           f'Нажми /go чтобы начать')
    
async def farewell(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')