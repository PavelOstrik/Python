from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5756852022:AAFlD8eMHltF4zLtp0LD-JwZznH21SPzQHc").build()

app.add_handler(CommandHandler("hi", hi_command))

print('server srart')
app.run_polling()