from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler, CallbackContext

import spoonacular as sp
import logging
from match_input import user_search


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Instantiate spoonacular api
api_instance = sp.API("7622a72decf948a0b1fb094128e2f884")

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def trivia_command(update: Update, context: CallbackContext) -> None:
    """Return a random food trivia."""
    try:
        # Get Random Food Trivia
        api_response = api_instance.get_random_food_trivia()
        result = api_response.json()['text']
        logging.info(f"Here is the result: {result}")

        return update.message.reply_text(result)
    except Exception as e:
        print("Exception when calling DefaultApi->get_random_food_trivia: %s\n" % e)

    update.message.reply_text(result)


def substitute(update: Update, context: CallbackContext) -> None:       
    """Return ingredient substitute(s)."""
    ingredient = update.message.text
    logger.info(f"Going to get {ingredient} substitutes...")

    # Query sqlite database for substitute(s)
    sub = user_search(ingredient)

    # Return formatted response

    # * TODO: Ask user for rating
    # TODO STEP 1: Query database to check if user has already rated

    # TODO STEP 2A: If rated already
    # if check_rating == True:
    # update.message.reply_text(text=sub, parse_mode = ParseMode.HTML)

    # * STEP 2B: Else haven't rated
    keyboard = [
        [
            InlineKeyboardButton("Useful", callback_data="Useful"),
            InlineKeyboardButton("Not Useful", callback_data="Not Useful"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(sub, parse_mode = ParseMode.HTML, reply_markup=reply_markup) 


def update_rating(update: Update, context: CallbackContext) -> None:
    """Update database with user's usefulness rating."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    reply = query.data

    # Reply with what the user selected
    query.edit_message_text(text=f"Selected option: {reply}")

    # TODO: Update the database with user's rating


def end(update: Update, context: CallbackContext) -> int:
    """/end will say bye if user wants to end the session."""

    # TODO: Tell bot to stop listening for input
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! See you again 😃')
