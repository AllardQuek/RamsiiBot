#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

from __future__ import print_function
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
                         CallbackQueryHandler, ConversationHandler, CallbackContext
from pprint import pprint
from commands import help_command, trivia_command, hungry_command, joke_command, \
                     substitute, update_rating
from general_helpers import start
from threading import Thread

import os
import logging
import json
import sys


PORT = int(os.environ.get('PORT', 5000))    # * For deploying to Heroku
TOKEN = os.getenv('TOKEN')                  # * To set the TOKEN environment variable
                                            # Locally: export TOKEN="<your_token>"
                                            # Heroku: heroku config:set TOKEN="<your_token"


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # For stopping the bot
    def end(update: Update, context: CallbackContext) -> int:
        """/end will say bye if user wants to end the session."""
        update.message.reply_video("https://media.giphy.com/media/ylyUQnaWJp7TRAGInK/giphy.mp4")

        # https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#simple-way-of-restarting-the-bot
        # TODO: add updater.start_polling() to /start as well and link with this
        # updater.stop()
        # os.execl(sys.executable, sys.executable, *sys.argv) Removed

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("trivia", trivia_command))
    dispatcher.add_handler(CommandHandler("hungry", hungry_command))
    dispatcher.add_handler(CommandHandler("joke", joke_command))
    dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CallbackQueryHandler(update_rating))

    # Any other message -> We treat as an ingredient substitution
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, substitute))

    # Start the Bot - for easier testing
    # updater.start_polling()

    # * For deploying to Heroku
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://hacknroll-2021.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
