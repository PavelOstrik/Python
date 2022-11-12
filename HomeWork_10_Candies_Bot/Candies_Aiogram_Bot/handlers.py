# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands

# На одну и ту же функцию можно повесить 2 команды
# Важно располагать команды по задуманнйо вами очереди выполнения
# commands=['start'] - /start  на этот триггер бот отреагирует выполнением привязанной
# к ней функции
# Важно писать команды одним словом
def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.WhoGoesFirst, commands=['go'])
    dp.register_message_handler(commands.userMove, commands=['user_move'])
    dp.register_message_handler(commands.botMove, commands=['bot_move'])
    dp.register_message_handler(commands.finish, commands=['finish'])
    dp.register_message_handler(commands.endGame, commands=['end_game'])
    dp.register_message_handler(commands.getNumber)