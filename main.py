import os
from dotenv import load_dotenv
import logging
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)


load_dotenv()
my_token = os.getenv("TOKEN")


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Responds to the user with a greeting, asking for their name.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Добрый день. Как вас зовут?"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Responds to user with a greeting containing their name and the current dollar rate.
    """
    
    name = update.message.text
    dollar_rate = get_dollar_rate()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Рад знакомству, {name}! Курс доллара сегодня {dollar_rate}р.",
    )


def get_dollar_rate():
    """
    Gets the current exchange rate of the US dollar to the Russian ruble
    from the official Central Bank of Russia API.

    Returns:
        float: Current exchange rate of the US dollar to the Russian ruble
    """
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    return data["Valute"]["USD"]["Value"]


if __name__ == "__main__":
    application = ApplicationBuilder().token(my_token).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
