'''
python: Main Shopping module

by Alexander Shinkov (@ashinkov)


TODO:
This can either be created from a list of ingredient tuples or initialized from a CSV file.
'''

import os
from decimal import Decimal
from python_shopping.ingredients import IngredientsStore
from python_shopping.cart import Cart
from python_shopping.discounts import BulkDiscount, NoDiscount

ingredients = [
    ('tomatoes', Decimal('0.15')),
    ('chicken', Decimal('3.49')),
    ('onions', Decimal('2.00')),
    ('rice', Decimal('0.70')),
              ]

# via .csv
csv_file_path = os.path.abspath('test.csv')
ingredient_store = IngredientsStore.init_from_file_path(csv_file_path)

# optionally via list of ingredient tuples
ingredient_store_2 = IngredientsStore(ingredients)


price = ingredient_store.get_ingredient_price('onions')
print(price)

shopping_cart = Cart(ingredient_store)

print(shopping_cart.ingredients_store.ingredients_map)


# adding 2 tomatoes...
# etc

shopping_cart.add('tomatoes',2)
shopping_cart.add('onions',3)
shopping_cart.add('onions',5)
shopping_cart.add('rice',1)

# shopping_cart.add('tomatoes',2)
# shopping_cart.subtract('tomatoes',2)
# print(shopping_cart.cart_map)

# calculating the price without discount
# = 17
print(shopping_cart.get_total())

# adding 2 discounts and 1 no discount (for test)
#
buy_one_get_one_free_tomatoes = BulkDiscount('tomatoes', 1, 1)
buy_two_get_third_free_onions = BulkDiscount('onions', 2, 1)
something_not_in_discount = NoDiscount('rice')

# :12.85 - (1+1 tomato and 2+1 onion)
# 17 - 0.015 (tomato) - 2 * 2 (onion) = 12.85
#
print(shopping_cart.get_total(discount_list=[buy_one_get_one_free_tomatoes,buy_two_get_third_free_onions]))

# with no discount (should be = with calculating the price without discount)
print(shopping_cart.get_total(discount_list=[something_not_in_discount]))


