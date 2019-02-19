'''
python: Ingredients Shopping module

by Alexander Shinkov (@ashinkov)

TODO:
Ingredients Shopping
Your task is to create a simple shopping cart to buy ingredients for our delicious recipes!
Ingredients are stored in a IngredientsStore object.
This can either be created from a list of ingredient tuples or initialized from a CSV file.
total = shopping_cart.get_total()

with discount
total_after_discount = shopping_cart.get_total(discounts=[discount_one, discount_two])
'''

import csv
from decimal import Decimal


class IngredientsStore:
    # Stores ingredients name and price

    # Create dict ingredients_map: name,price
    #
    ingredients_map = {}

    # via  list of ingredient tuples
    #
    def __init__(self, ingredients_list_of_tuple=None):

        # to be able to proceed with empty list
        #
        self.ingredients_map = dict() if ingredients_list_of_tuple is None \
                                      else dict(ingredients_list_of_tuple)

    # via .csv (1- name; 2- price):
    #
    @classmethod
    def init_from_file_path(self, path_to_ingredient_csv):

        # open .csv in read-only
        #
        with open(path_to_ingredient_csv, mode='r') as csvFile:
            reader = csv.reader(csvFile)

            # create dict: ingredients_map
            # from all rows in .csv
            # 1 column - ingredient_name: rows[0]- taking 'as is'
            # 2 column - creating decimal instance: Decimal(rows[1]
            #
            ingredients_map = {rows[0]: Decimal(rows[1]) for rows in reader}
            return self(ingredients_map)

    # get price from dict using key=ingredient_name
    #
    def get_ingredient_price(self, ingredient_name):
        return self.ingredients_map.get(ingredient_name)

