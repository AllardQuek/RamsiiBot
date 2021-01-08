from sqlalchemy import create_engine
from ratings import percentage_rating

engine = create_engine('sqlite:///ingredient_list.db')      # Access ingredient list

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
                USER_RATING = "<b>" + PERCENTAGE_RATING + "%</b> of users found this information useful."

                if row['ing_cs'] == "NIL":
                    CS = ""
                else:
                    CS = "\n\nYou can closely substitute " + row['orig_unit'] + " " + row['ing_input'] + " with <b>" + row['ing_cs'] + "</b>."
                
                if row['ing_sp'] == "NIL":
                    SP = ""
                else:
                    SP = "\n\nYou can make " + row['orig_unit'] + " " + row['ing_input'] + " with <b>" + row['ing_sp'] + "</b>."
                
                if row['ing_alt'] == "NIL":
                    ALT = ""
                else:
                    ALT = "\n\nYou can entirely replace " + row['orig_unit'] + " " + row['ing_input'] + " with <b>" + row['ing_alt'] + "</b>."
                
                if row['isVegan'] == 'Yes':
                    VEG = "\n<i>Vegan</i>"
                elif row['isVegan'] == 'No':
                    VEG = "\n<i>Non-vegan</i>"
                else:
                    VEG = "\n<i>May or may not be vegan</i>"

                return TITLE + VEG + CS + SP + ALT + SEPARATOR + USER_RATING

        if search_failure:
            return "Ingredient cannot be found! Please try again."