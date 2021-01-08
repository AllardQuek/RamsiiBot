#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.


from __future__ import print_function
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler, CallbackContext
from pprint import pprint
from commands import help_command, trivia_command, hungry_command, joke_command, substitute, end, update_rating
from general_helpers import start

import os
import logging


PORT = int(os.environ.get('PORT', 5000))
TOKEN = "1496622121:AAH90cjwm_Og9oPuWenRmS0peC4TRKxBMNs"


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # On different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("trivia", trivia_command))
    dispatcher.add_handler(CommandHandler("hungry", hungry_command))
    dispatcher.add_handler(CommandHandler("joke", joke_command))
    dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CallbackQueryHandler(update_rating))

    # Any other message -> We treat as an ingredient substitution
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, substitute))


    # Start the Bot
    updater.start_polling()

    # * For deploying to Heroku
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