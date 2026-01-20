from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am your bot 🤖")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"You said: {update.message.text}")

if __name__ == '__main__':
    app = ApplicationBuilder().token('8324862269:AAEA4U6urK4b0Y1HYfuBeOf4QSuhJ_c_Ick').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    print("Bot is running...")
    app.run_polling()
