from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    log(update, context)   
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    # Возьмём сообщение пользователя и положим её в отдельную переменную
    msg = update.message.text
    print(msg)
    # Теперь нам надо разобрать наше текстовое сообщение
    items = msg.split()  # /sum, какое то число, какое то число
    x = int(items[1])
    y = int(items[2]) 
    # Если мы хотим добавить обработку ошибок ввода, это все нужно описывать в рамках
    # данного метода, если мы не получили x или y, или если они не int
    
    await update.message.reply_text(f'{x} + {y} = {x+y}')  