from sqlalchemy import create_engine

engine = create_engine('sqlite:///ingredient_list.db')  # accesses ingredient list


def userSearch(user_input):
    with engine.connect() as connection:
        result = connection.execute("select ing_input from ingredient_substitution")
        searchFailure = True
        for row in result:
            if user_input.lower() == str(row['ing_input']):
                print("Success")
                searchFailure = False
                break
        if searchFailure:
            print("Ingredient cannot be found! Please try another one.")
