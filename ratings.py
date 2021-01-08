from sqlalchemy import create_engine, insert, text

engine = create_engine('sqlite:///ingredient_list.db')  # accesses ingredient list


def check_rating(user_id, user_input):
    ALREADY_RATED = False  # determines whether the inline keyboard for ratings appear or not
    with engine.connect() as connection:
        # Searches each row of the db to access the relevant data
        result = connection.execute("select * from raters")
        for row in result:
            if user_id == row['id'] and user_input == row['rated_ing']:
                ALREADY_RATED = True
                return ALREADY_RATED
            else:
                return ALREADY_RATED


def positive_rating(user_id, ing):
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
