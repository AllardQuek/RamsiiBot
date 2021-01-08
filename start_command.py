from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    name = update.message.chat.first_name

    intro = f"Hi {name}! I'm <b>Ramsay</b>, the best chef in the world with 7 Michelin stars! Missing an ingredient for your recipe? What ingredient are you having a hard time finding? (Or if you're bored, try /trivia to get random food trivia!)"

    return update.message.reply_text(text=intro, parse_mode= ParseMode.HTML)
