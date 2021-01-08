from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from match_input import userSearch

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    username = update.message.chat.username
    # intro = f"Hi {username}! I'm Ramsay, the best chef in the world with 7 Michelin 🌟s! Missing an ingredient for your recipe? Let me find you a /substitute right away! Or if you're bored, try /trivia to get a random trivia!"

    intro = input(f"""
        Hi {username}! I'm Ramsay, the best chef in the world with 7 Michelin stars! 
        Missing an ingredient for your recipe? What ingredient are you having a hard time finding?
        (Or if you're bored, try /trivia to get random food trivia!)
    """)

    userSearch(intro)

    keyboard = [
        [
            # InlineKeyboardButton("Substitute Ingredient", callback_data='/substitute'),
            InlineKeyboardButton("Trivia", callback_data='/trivia'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(intro, reply_markup=reply_markup)              
