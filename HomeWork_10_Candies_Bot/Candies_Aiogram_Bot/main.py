#здесь главный файл для запуска

from aiogram.utils import executor

import handlers
from bot import dp


async def on_startup(_):
    print('Бот запущен')

handlers.registred_handlers(dp)

# Начинаем получать сообщения и все события
# skip_updates=True пишем, чтобы игнорировать сообщения пользователей, когда бот не запущен
# on_startup функция сигнализирующая нам о запуске нашего бота
# if __name__ == '__main__': пишем, чтобы бот запускался только из модуля main
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)