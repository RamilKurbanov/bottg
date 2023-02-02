from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from controller import *
from spy import *
from search import *


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


app = ApplicationBuilder().token("5827588218:AAEYb8_c-uipPrfNo2xa9y5UhIfESqI87ig").build()

app.add_handler(CommandHandler("Hello", hello))
app.add_handler(CommandHandler("start", help))
app.add_handler(CommandHandler("code", code))
app.add_handler(CommandHandler("10", codeten))
app.add_handler(CommandHandler("15", fefteen))
app.add_handler(CommandHandler("20", twenty))
app.add_handler(CommandHandler("search", search))




app.run_polling()