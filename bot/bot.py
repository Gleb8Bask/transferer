import os

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import message_texts
from dotenv import load_dotenv

import get_summarize
import asyncio

def configure():
    load_dotenv()


configure()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    exit("specify TELEGRAM_BOT_TOKEN env variable")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat is None")
        return
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=message_texts.GREETINGS)


async def summarize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat is None in /summarize")
        return
    sums = await get_summarize.get_summarize()
    response = ",".join((str(sums.message) for sums in sums))
    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=response)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    summarize_handler = CommandHandler('summarize', summarize)
    application.add_handler(summarize_handler)

    application.run_polling()
