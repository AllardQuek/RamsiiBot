from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

import spoonacular as sp
import logging


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Instantiate spoonacular api
api_instance = sp.API("7622a72decf948a0b1fb094128e2f884")

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
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
    update.message.reply_text(f"You asked for {ingredient} substitutes.")

    # TODO: Query sqllite database for substitute(s)


    # TODO: Return formatted response


def cancel(update: Update, context: CallbackContext) -> int:
    # TODO: Type /cancel to stop conversation by saying 'Bye'
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! See you again 😃', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END