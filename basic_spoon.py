from __future__ import print_function
import spoonacular as sp
from pprint import pprint


api = sp.API("7622a72decf948a0b1fb094128e2f884")

# Parse an ingredient
response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
data = response.json()
print(data[0]['name'])

# Detect text for mentions of food
response = api.detect_food_in_text("I really want a cheeseburger.")
data = response.json()
print(data['annotations'][0])

# Get a random food joke
response = api.get_a_random_food_joke()
data = response.json()
print(data['text'])


# Get ingredient substitution for butter
ingredient_name = 'butter' # str | The name of the ingredient you want to replace.

try:
    # Get Ingredient Substitutes
    api_response = api.get_ingredient_substitutes(ingredient_name)
    pprint(api_response.text)
except Exception as e:    # except ApiException as e:
    print("Exception when calling DefaultApi->get_ingredient_substitutes: %s\n" % e)