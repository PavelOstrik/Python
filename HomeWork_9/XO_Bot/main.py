from aiogram import Bot, types
# types специальные типы данных, чтобы мы могли писать аннотации типов в наших функциях
from aiogram.dispatcher import Dispatcher  
# Dispatcher класс, который позволяет улавливать отправку сообщений боту и
# соответствующим образом их прорабатывать, его реакцию мы прописываем 
from aiogram.utils import executor
# executor чтобы мы могли запустить нашего бота, чтобы он вышел в онлайн
import os
# Чтобы мы могли прочитать наш токен
from config import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import random

bot = Bot(Token)
dp = Dispatcher(bot)
item = {}
gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]

CrossesOrToe = ["0", "X"]
playerSymbol = CrossesOrToe[random.randint(0, 1)]

botSymbol = ""
if (playerSymbol == "0"):
    botSymbol = "X"
else:
    botSymbol = "0"
    
winbool = False

losebool = False

def clear():
    global gameGround
    gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]


def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        print("win")
        global winbool
        winbool = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        print("lose")
        global losebool
        losebool = True


def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol

@dp.message_handler(commands=['start'])
async def start_mesage(message:types.Message):
    chat_id = message.chat.id  # идентификатор чата
    username = message.from_user.first_name # Получаем имя пользователя
# Функция send_message принимает идентификатор чата (берем его из сообщения) и текст для отправки.
    await bot.send_message(chat_id, f'Привет {username}, сейчас я тебя выиграю в крестики/нолики!')
    # keyboard
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)                                    
    global markup
    markup = types.InlineKeyboardMarkup(row_width=3)
    # item = {}
    i = 0

    for i in range(9):
        item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

    markup.row(item[0], item[1], item[2])
    markup.row(item[3], item[4], item[5])
    markup.row(item[6], item[7], item[8])
    await bot.send_message(message.chat.id, "Выбери клетку", reply_markup=markup)

@dp.callback_query_handler(func=lambda call: True)
async def callbackInline(call):
    if (call.message):

        # bot manager
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol
        # player manager
        for i in range(9):
            if call.data == str(i):
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol

            # lose or win
            win(gameGround[0], gameGround[1], gameGround[2])
            win(gameGround[0], gameGround[4], gameGround[8])
            win(gameGround[6], gameGround[4], gameGround[2])
            win(gameGround[6], gameGround[7], gameGround[8])
            win(gameGround[0], gameGround[3], gameGround[6])
            lose(gameGround[0], gameGround[1], gameGround[2])
            lose(gameGround[0], gameGround[4], gameGround[8])
            lose(gameGround[6], gameGround[4], gameGround[2])
            lose(gameGround[6], gameGround[7], gameGround[8])
            lose(gameGround[0], gameGround[3], gameGround[6])

            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики нолики",
                              reply_markup=None)
        # update cells
        global  markup
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])

        await bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)
        global winbool
        if winbool:
            clear()
            await bot.send_message(call.message.chat.id, "Я проиграл :(")

            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            await bot.send_message(call.message.chat.id, "Я выиграл!!")


            losebool = False
            gameIsStart = False   

if __name__ == '__main__':
    executor.start_polling(dp)