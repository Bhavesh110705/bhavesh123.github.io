import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import nest_asyncio

# Fix for nested event loops
nest_asyncio.apply()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Your Telegram Bot Token
BOT_TOKEN = '8056347442:AAGDg5spzxlxXIBoaCLP9io2KblUnbcfaaQ'

# Dictionary of download links hosted on your website
papers = {
    "class9": {
        "science": "https://look.ct.ws/papers/class9/Science.pdf",
        "retail": "https://look.ct.ws/papers/class9/Retail.pdf",
        "it": "https://look.ct.ws/papers/class9/IT.pdf",
        "automotive": "https://look.ct.ws/papers/class9/Automotive.pdf"
    },
    "class10": {
        "math_basic": "https://look.ct.ws/papers/class10/MathBasic.pdf",
        "math_standard": "https://look.ct.ws/papers/class10/MathStandard.pdf",
        "science": "https://look.ct.ws/papers/class10/Science.pdf",
        "english": "https://look.ct.ws/papers/class10/English.pdf",
        "social_science": "https://look.ct.ws/papers/class10/SocialScience.pdf",
        "computer": "https://look.ct.ws/papers/class10/Computer.pdf"
    },
    "class11": {
        "multimedia": "https://look.ct.ws/papers/class11/Multimedia.pdf",
        "food_production": "https://look.ct.ws/papers/class11/FoodProduction.pdf",
        "retail": "https://look.ct.ws/papers/class11/Retail.pdf"
    },
    "class12": {
        "math": "https://look.ct.ws/papers/class12/Math.pdf",
        "biology": "https://look.ct.ws/papers/class12/Biology.pdf",
        "history": "https://look.ct.ws/papers/class12/History.pdf",
        "english": "https://look.ct.ws/papers/class12/English.pdf",
        "economics": "https://look.ct.ws/papers/class12/Economics.pdf",
        "computer_science": "https://look.ct.ws/papers/class12/ComputerScience.pdf",
        "psychology": "https://look.ct.ws/papers/class12/Psychology.pdf",
        "sociology": "https://look.ct.ws/papers/class12/Sociology.pdf"
    }
}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! 🎓\nUse the command like this:\n/get_papers class10 math\n\nAvailable classes: class9, class10, class11, class12"
    )

# Get papers command
async def send_question_paper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("❗ Use: /get_papers class10 math")
        return

    class_name = context.args[0].lower()
    subject = "_".join(context.args[1:]).lower()

    if class_name in papers and subject in papers[class_name]:
        link = papers[class_name][subject]
        await update.message.reply_text(f"📄 Your download link:\n{link}")
    else:
        await update.message.reply_text("⚠️ No paper found. Please check class or subject.")

# Error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

# Main function
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("get_papers", send_question_paper))
    app.add_error_handler(error_handler)

    await app.bot.set_my_commands([
        ("start", "Start the bot"),
        ("get_papers", "Get question paper (e.g. /get_papers class10 math_basic)")
    ])

    await app.run_polling()

# Run
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
