# Здесь что-то типа контроллера связывающий хендлеры и вью

# Импортируем types чтобы нам была доступна работа с типами
from aiogram import types

import view
import model
import random
from bot import bot

# Внутри аcинхронной функции вызываем метод с помощью await
# Указываем types.Message чтобы нам был доступен весь перечень встроенных методов
async def start(message: types.Message):
    await view.greetings(message)
    
async def finish(message: types.Message):
    await view.farewell(message)
    
async def endGame(message: types.Message):
    model.candies = 150
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, игра закончилась, нажми:\n'
                           f'/start - получить стартовые инструкции\n'
                           f'/go - начать игру\n'
                           f'/finish - и я с тобой попрощаюсь')
 
async def getNumber(message: types.Message):
    number = message.text
    if 0 < int(number) < 29:
        model.setTake(int(number))
        await bot.send_message(message.from_user.id,
                               f'Нажми /user_move')
 
    else:
        await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')
        
    
async def botMove(message: types.Message):
    candies = model.getCandies()
    take = random.randint(1,28)
    count = candies - take    
    model.setCandies(count)
    model.getCandies()
    await bot.send_message(message.from_user.id,
                        f'Я взял {take} конфет, осталось {model.getCandies()}!')
                        
    if model.checkWin() == True:
        await bot.send_message(message.from_user.id, 
                                f'{message.from_user.first_name}, ты выиграл')
        await endGame(message)
    else:
        await bot.send_message(message.from_user.id,
                            f'{message.from_user.first_name}, теперь ты берешь конфеты\n'
                            f'Введи количество конфет от 1 до 28')
        
        
async def userMove(message: types.Message): 
    take = model.getTake()    
    candies = model.getCandies()    
    count = candies - take
    model.setCandies(count)
    model.getCandies()
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, ты взял {take} конфет, осталось {model.getCandies()}!\n'
                        )

    if model.checkWin() == True:
        await bot.send_message(message.from_user.id, 
                                f'{message.from_user.first_name}, Я, Великий Бот, выиграл')                                
        await endGame(message)
    else:
        await bot.send_message(message.from_user.id,
                               f'Теперь я беру конфеты\n'
                               f'Нажми /bot_move, помоги мне, а то у меня лапки') 
                          

        
async def WhoGoesFirst(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Начальное кол-во конфет = {model.getCandies()}')
    model.setFirstMove()
    if model.getFirstMove() == 1:    
        await bot.send_message(message.from_user.id, 
                           f'{message.from_user.first_name}, ты берешь конфеты первый!\n'
                           f'Введи количество конфет от 1 до 28')

    else:
        await bot.send_message(message.from_user.id,
                               f'Я, Великий Бот, беру конфеты первый\n'
                               f'Нажми /bot_move, помоги мне, а то у меня лапки')