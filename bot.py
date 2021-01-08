#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""


from __future__ import print_function
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pprint import pprint
import os
import spoonacular as sp
from help_command import help_command

api_instance = sp.API("7622a72decf948a0b1fb094128e2f884")


PORT = int(os.environ.get('PORT', 5000))
TOKEN = "1194072377:AAFlyOFCsubC_G5zhQAGfzeHfyvUrMuKxzk"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    username = update.message.chat.username

    intro = f"""
        Hi {username}! I'm Ramsay, the best chef in the world with 7 Michelin stars! 
        Missing an ingredient for your recipe? Let me find you a substitute right away!
        Or if you're bored, try /trivia to get a random trivia!
    """

    update.message.reply_text(intro)              

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def trivia_command(update: Update, context: CallbackContext) -> None:
    """Return a random food trivia."""
    try:
        # Get Random Food Trivia
        api_response = api_instance.get_random_food_trivia()
        result = api_response.json()['text']
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_random_food_trivia: %s\n" % e)

    update.message.reply_text(result)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("trivia", trivia_command))


    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN)
    # updater.bot.setWebhook('https://hacknroll-2021.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()