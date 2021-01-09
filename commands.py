from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler, CallbackContext
from general_helpers import user_search
from threading import Thread

import logging
import ratings
import spoonacular as sp


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Instantiate spoonacular api
api_instance = sp.API("7622a72decf948a0b1fb094128e2f884")

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""

    command_options = "As your gastronomic companion, there many things I can do. You can use these anytime.\n\n<b>substitute</b> (Type an ingredient in chat): Where's the <i>LAMB SAUCE?</i>\n<b>/trivia</b>: Don't be an idiot sandwich.\n<b>/hungry</b>: It's delicious.\n<b>/joke</b>: Very funny!\n<b>/end</b>: **** me, what do you think?"
    update.message.reply_text(command_options, parse_mode=ParseMode.HTML)


def trivia_command(update: Update, context: CallbackContext) -> None:
    """Return a random food trivia."""
    try:
        # Get Random food trivia
        api_response = api_instance.get_random_food_trivia()
        result = "Here's a touch of <b>Ramsii's knowledge</b> for you.\n\n" + api_response.json()['text']
        logger.info(f"Here is the result: {result}")

        update.message.reply_text(result, parse_mode=ParseMode.HTML)
    except Exception as e:
        print("Exception when calling DefaultApi->get_random_food_trivia: %s\n" % e)


def substitute(update: Update, context: CallbackContext) -> None:
    """Return ingredient substitute(s)."""
    ingredient = update.message.text         # String
    user_id = update.message.from_user.id    # Integer
    logger.info(f"Going to get {ingredient} substitutes...")

    # Query sqlite database for substitute(s)
    sub = user_search(f'{ingredient}')

    if not sub:
        # If sub turns out to be the empty string, means we found no results from our database
        sub = "What <i>is</i> this? Try something else."
        update.message.reply_text(sub, parse_mode=ParseMode.HTML)

        # Reply to user and exit from function
        return

    # If we did get a result from our database, query db to check if user has already rated it
    rated = ratings.check_rating(str(user_id), ingredient)     
    
    if rated == True:
        # Return results and prompt for next substitution
        update.message.reply_text(text=sub, parse_mode = ParseMode.HTML)
        update.message.reply_text(text="Right, what else do you want to substitute?")
    else:
        keyboard = [
            [
                InlineKeyboardButton("Useful", callback_data=f"Useful {ingredient}"),
                InlineKeyboardButton("Not Useful", callback_data=f"Not Useful {ingredient}"),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        # Return results and prompt user for usefulness rating with an in-line keyboard
        update.message.reply_text(sub, parse_mode = ParseMode.HTML, reply_markup=reply_markup)


def hungry_command(update: Update, context: CallbackContext) -> None:
    """Return a random recipe."""
    try:
        # Query for random recipe
        # api_response = api_instance.get_random_recipes(limit_license=limit_license, tags=tags, number=number)
        api_response = api_instance.get_random_recipes(number=1)
        recipe_res = api_response.json()['recipes'][0]
        logger.info(f"Here is the response: {api_response}")

        title = recipe_res['title'].upper()
        image = recipe_res['image']
        url = recipe_res['spoonacularSourceUrl']

        update.message.reply_text(f"Gorgeous. Here's something for you to think about.\n\n<b>{title}</b> {url}", parse_mode=ParseMode.HTML)
        update.message.reply_photo(image)
    except Exception as e:
        print("Exception when calling DefaultApi->get_random_food_trivia: %s\n" % e)


def joke_command(update: Update, context: CallbackContext) -> None:
    """Return a random food joke."""
    try:
        # Get a random food joke
        response = api_instance.get_a_random_food_joke()
        data = response.json()
        joke = "Laugh a bit, will ya?\n\n" + data['text']
        logger.info(f"Here is the response: {response}")

        update.message.reply_text(joke)
    except Exception as e:
        print("Exception when calling DefaultApi->get_random_food_trivia: %s\n" % e)


def update_rating(update: Update, context: CallbackContext) -> None:
    """Update database with user's usefulness rating."""
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    reply_list = query.data.split()

    # Extract callback data: usefulness and ingredient
    if reply_list[0] == "Useful":
        usefulness = "Useful"
        ingredient = " ".join(reply_list[1:])
    else:
        usefulness = "Not Useful"
        ingredient = " ".join(reply_list[2:])

    # Reply with what the user selected
    reply_markup = InlineKeyboardMarkup([])
    query.edit_message_reply_markup(reply_markup)
    query.message.reply_text(text=f"Thanks for your feedback. \n\nNow, what else do you want to substitute?")

    user_id = query.from_user.id    # Integer

    # Update the database with user's rating
    if usefulness == "Useful":
        logger.info("Adding positive rating...")
        ratings.positive_rating(str(user_id), ingredient)      
    else:
        logger.info("Adding negative rating...")
        ratings.negative_rating(str(user_id), ingredient)


# TODO: Add user suggestions to our database
# def suggest(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f"Type your suggestion below, and we will look into it.")