# Telegram Bot for getting USD exchange rate

This is a simple Telegram bot written in Python that responds to user
messages with a greeting containing their name and the current exchange
rate of the US dollar to the Russian ruble. The bot uses the official
Central Bank of Russia API to get the current exchange rate.

The bot is running on a server and is accessible via Telegram messenger
at @USDExchangeRateBot.

## How to use

1. Start a conversation with the bot by sending it a message with your
   name.
2. The bot will respond with a greeting containing your name and the
   current exchange rate of the US dollar to the Russian ruble.

## How to run

This bot is designed to be run on a server. To run it, you will need to
have Python installed on your server, as well as the `python-telegram-bot`
library. The bot can be started by running the `main.py` file with
Python.

You will also need to set the `TOKEN` environment variable to your bot's
token. This can be obtained by talking to the BotFather bot in Telegram.

## License

This code is licensed under the MIT license. See the `LICENSE` file for
details.
