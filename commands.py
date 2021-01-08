from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import spoonacular as sp


api_instance = sp.API("7622a72decf948a0b1fb094128e2f884")

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def trivia_command(update: Update, context: CallbackContext) -> None:
    """Return a random food trivia."""
    try:
        # Get Random Food Trivia
        api_response = api_instance.get_random_food_trivia()
        result = api_response.json()['text']
        print(result)
        
        return update.message.reply_text(result)
    except Exception as e:
        print("Exception when calling DefaultApi->get_random_food_trivia: %s\n" % e)

    update.message.reply_text(result)