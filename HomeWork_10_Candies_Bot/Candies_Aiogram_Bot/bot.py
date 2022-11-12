#Здесь создается бот и хранится его токен


from aiogram import Bot
from aiogram.dispatcher import Dispatcher

#name_bot = Candy_Survival_Game_Bot
bot = Bot(token='5668585253:AAFK6lEGWpezL3Ys7DEw2DT7tG10AFsohxw')
dp = Dispatcher(bot)
# Dispatcher принимает все апдейты и обрабатывает их. Наш слушатель, принимает 
# сообщения от пользователя