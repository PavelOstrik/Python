from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Здесь мы делаем метод обёртку над командами

def log(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    with open('db.csv', 'a', encoding='UTF-8') as file: #Создаём файл
        # Прописываем какую информацию будем логировать
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, \n')
    
    