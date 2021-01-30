from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, \
    MessageHandler, Filters
from additional.log_orm import DuckLogger


class DUCKBot:
    def __init__(self):
        self.mybot = Updater("1496953470:AAG4_eCMycKNHmHc4UG7rptNrWjyRz-LLXQ")
        self.log = DuckLogger(self)

    def bot_update(self):
        dp = self.mybot.dispatcher
        dp.add_handler(CommandHandler("start", self.greet_user))
        dp.add_handler(MessageHandler(Filters.text, self.talk_to_me))
        self.mybot.start_polling()
        self.mybot.idle()

    def greet_user(self, update: Update, context: CallbackContext):
        text: str = f"Welcome to the Duck world!"
        update.message.reply_text(text)
        self.log.debug(f'the reply is: {text}')

    def talk_to_me(self, update: Update, context: CallbackContext):
        user_text = f"Hello, my friend, {update.message.chat.username}. \
    Here is your message: {update.message.text}"
        update.message.reply_text(user_text)


if __name__ == "__main__":
    duck_bot = DUCKBot()
    duck_bot.bot_update()
