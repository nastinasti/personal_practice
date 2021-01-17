from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, \
    MessageHandler, Filters
from log_orm import DuckLogger
import logging



def bot_update():
    mybot = Updater("1496953470:AAG4_eCMycKNHmHc4UG7rptNrWjyRz-LLXQ")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


def greet_user(update: Update, context: CallbackContext):
    text: str = f"Welcome to the Duck world!"
    update.message.reply_text(text)
    log = DuckLogger(logging)
    log.logger.info(text)


def talk_to_me(update: Update, context: CallbackContext):
    user_text = f"Hello, my friend, {update.message.chat.username}. \
Here is your message: {update.message.text}"
    log = DuckLogger(logging)
    log.logger.info(update.message)
    update.message.reply_text(user_text)


if __name__ == "__main__":
    bot_update()
