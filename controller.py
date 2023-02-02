from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


async def help (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi /code')

async def code (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Enter the code of the desired movie ')


