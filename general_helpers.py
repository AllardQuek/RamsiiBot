from sqlalchemy import create_engine
from ratings import percentage_rating
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

engine = create_engine('sqlite:///ingredient_list.db')      # Access ingredient list

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    name = update.message.chat.first_name

    intro = f"Hi {name}! I'm <b>Ramsay</b>, the best chef in the world with 7 Michelin stars! \nMissing an ingredient for your recipe? What ingredient are you having a hard time finding? (Or if you're bored, try /trivia to get random food trivia!)"

    return update.message.reply_text(text=intro, parse_mode= ParseMode.HTML)


def user_search(user_input):
    with engine.connect() as connection:
        # Searches each row of the db to access the relevant data
        result = connection.execute("select * from ingredient_substitution")
        search_failure = True

        CS = ""     # Close substitutes
        SP = ""     # Self-produce
        ALT = ""    # Alternatives
        VEG = ""    # Is Vegan

        for row in result:
            if user_input.lower() == row['ing_input']:				
                search_failure = False
                TITLE = "<b><u>" + row['full_ing'].upper() + "</u></b>"
                PERCENTAGE_RATING = str(percentage_rating(user_input))
                SEPARATOR = "\n\n\n---------------------\n\n"
                USER_RATING = ""
                if PERCENTAGE_RATING == "0":
                    USER_RATING = "No users found this information useful."
                else:
                    USER_RATING = "<b>" + PERCENTAGE_RATING + "%</b> of users found this information useful."

                if row['ing_cs'] == "NIL":
                    CS = ""
                else:
                    CS = "\n\nYou can closely substitute " + str(row['orig_unit']) + " " + row['ing_input'] + " with <b>" + row['ing_cs'] + "</b>."
                
                if row['ing_sp'] == "NIL":
                    SP = ""
                else:
                    SP = "\n\nYou can make " + str(row['orig_unit']) + " " + row['ing_input'] + " with <b>" + row['ing_sp'] + "</b>."
                
                if row['ing_alt'] == "NIL":
                    ALT = ""
                else:
                    ALT = "\n\nYou can entirely replace " + str(row['orig_unit']) + " " + row['ing_input'] + " with <b>" + row['ing_alt'] + "</b>."
                
                if row['isVegan'] == 'Yes':
                    VEG = "\n<i>Vegan</i>"
                elif row['isVegan'] == 'No':
                    VEG = "\n<i>Non-vegan</i>"
                else:
                    VEG = "\n<i>May or may not be vegan</i>"

                return TITLE + VEG + CS + SP + ALT + SEPARATOR + USER_RATING

        if search_failure:
            return "Ingredient cannot be found! Please try again."


# def suggestion():
# TODO: suggestions at failure state and not useful state