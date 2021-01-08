from sqlalchemy import create_engine

engine = create_engine('sqlite:///ingredient_list.db')  # accesses ingredient list


def userSearch(user_input):
    with engine.connect() as connection:
        result = connection.execute("select * from ingredient_substitution")
        searchFailure = True
        cs = ""
        sp = ""
        alt = ""
        for row in result:
            if user_input.lower() == row['ing_input']:				#searches each row of the db to access the relevant data
                searchFailure = False
                if row['ing_cs'] == "NIL":
                    cs = ""
                else:
                    cs = "\n" + row['ing_cs']
                if row['ing_sp'] == "NIL":
                    sp = ""
                else:
                    sp = "\n" + row['ing_sp']
                if row['ing_alt'] == "NIL":
                    alt = ""
                else:
                    alt = "\n" + row['ing_alt']
                print(row['full_ing'] + cs + sp + alt)

        if searchFailure:
            print("Ingredient cannot be found! Please try another one.")
