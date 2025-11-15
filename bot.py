
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8416295389:AAFy8aio-OTXglDufmWN6xNekvpn4-BNffU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 قناة التيليغرام", url="https://t.me/fxtraderchanel")],
        [InlineKeyboardButton("🛠 حسابات الدعم", url="https://t.me/FsupportX")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("اهلا!", reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
