from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from controller import *


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


app = ApplicationBuilder().token("5827588218:AAEYb8_c-uipPrfNo2xa9y5UhIfESqI87ig").build()

app.add_handler(CommandHandler("Hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("code", code))
# app.add_handler(CommandHandler("Hello", hello))



app.run_polling()