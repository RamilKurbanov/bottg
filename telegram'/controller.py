from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *

async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_message (update, context)
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


async def help (update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_message (update, context)
    await update.message.reply_text(f'/hi\n/code\n/10 - Hachiko: The Most Faithful Friend (2008)\n/15 -Vavilon(2022)\n/20 - Lulu and Brigs(2022) ')

async def code (update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_message (update, context)
    await update.message.reply_text(f'Enter the code of the desired movie ')

async def codeten (update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_message (update, context)
    await update.message.reply_text(f'Hachiko: The Most Faithful Friend (2008) - https://www.kinopoisk.ru/film/387556/ ')

async def fefteen (update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_message (update, context)
    await update.message.reply_text(f'Vavilon(2022) - https://www.kinopoisk.ru/film/102125/ ')

async def twenty (update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_message (update, context)
    await update.message.reply_text(f'Lulu and Brigs(2022) - https://www.kinopoisk.ru/film/1355139/ ')

async def search (update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_message (update, context)
    import search


    


