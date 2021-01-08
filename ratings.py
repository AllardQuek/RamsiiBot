from sqlalchemy import create_engine, insert, text


engine = create_engine('sqlite:///ingredient_list.db')  # Access ingredient list

def check_rating(user_id, user_input):
    """Check if user has already rated an ingredient substitution."""
    ALREADY_RATED = False    # Determines whether the inline keyboard for ratings appear or not

    with engine.connect() as connection:
        # Searches each row of the db to access the relevant data
        result = connection.execute("select * from raters")
        for row in result:
            if user_id == row['id'] and user_input == row['rated_ing']:
                ALREADY_RATED = True
        return ALREADY_RATED


def positive_rating(user_id, ing):
    """Update database with positive rating for user."""
    with engine.connect() as connection:
        # Searches each row of the db to access the relevant data
        ins_data = {"id": user_id, "rated_ing": ing}
        ins_statement = text("""insert into raters(id, rated_ing) values(:id, :rated_ing)""")
        connection.execute(ins_statement, **ins_data)
        update_rating = connection.execute("select * from ingredient_substitution")

        for row in update_rating:
            if ing.lower() == row['ing_input']:
                CURRENT_RATING = int(row['rating']) + 1
                CURRENT_RATER_NUMBER = int(row['raters']) + 1
                connection.execute(f"update ingredient_substitution set rating={CURRENT_RATING} where id={row['id']}")
                connection.execute(f"update ingredient_substitution set raters={CURRENT_RATER_NUMBER} where id={row['id']}")


def negative_rating(user_id, ing):
    """Update database with negative rating for user."""
    with engine.connect() as connection:
        # Searches each row of the db to access the relevant data
        ins_data = {"id": user_id, "rated_ing": ing}
        ins_statement = text("""insert into raters(id, rated_ing) values(:id, :rated_ing)""")
        connection.execute(ins_statement, **ins_data)
        update_rating = connection.execute("select * from ingredient_substitution")
        
        for row in update_rating:
            if ing.lower() == row['ing_input']:
                CURRENT_RATER_NUMBER = int(row['raters']) + 1
                connection.execute(f"update ingredient_substitution set raters={CURRENT_RATER_NUMBER} where id={row['id']}")

def percentage_rating(user_input):
    with engine.connect() as connection:
        result = connection.execute("select * from ingredient_substitution")
        NO_OF_RATINGS = 0  # ratings number
        NO_OF_RATERS = 0  # raters number
        PERCENTAGE = 0.0    # 'like' percentage

        for row in result:
            if user_input.lower() == row['ing_input']:
                NO_OF_RATINGS = int(row['rating'])
                NO_OF_RATERS = int(row['raters'])
                try:
                    PERCENTAGE = (NO_OF_RATINGS/NO_OF_RATERS) * 100
                    PERCENTAGE = round(PERCENTAGE, 1)
                except ZeroDivisionError:
                    PERCENTAGE = 0
        return PERCENTAGE

