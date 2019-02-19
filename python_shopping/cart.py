'''
python: Shopping Cart module

by Alexander Shinkov (@ashinkov)

TODO:
Carts should be created with an IngredientsStore instance.

from cart import Cart

shopping_cart = Cart(ingredient_store)
Ingredients can be added to a cart by name, with an optional quantity parameter.

shopping_cart.add('tomatoes')
shopping_cart.add('onions', 3)

The total for the cart can be calculated with get_total().
This method optionally takes a list of Discount objects that are applied
to items in the cart when calculating the total.

'''

from python_shopping.ingredients import IngredientsStore


class Cart:

    # Create dict cart_map: ingredient_name, number_of_items
    #
    cart_map = {}

    # getting ingredient dictionary from ingredients
    #
    def __init__(self, ingredient_store):
        self.ingredients_store = ingredient_store

    # 1st method - adding ingredient_name + number_of_items to cart (default number_of_items=1)
    #
    def add(self, ingredient_name, number_of_items=1):

        # checking/proceeding with positive number_of_items
        #
        if number_of_items > 0:

            # if ingredient_name exists in ingredients_store
            #
            if ingredient_name in self.ingredients_store.ingredients_map.keys():

                # if ingredient_name exists in our cart_map then +number_of_items
                # (+1 by default if no number_of_items mentioned)
                #
                if ingredient_name in self.cart_map.keys():
                    self.cart_map[ingredient_name] = self.cart_map.get(ingredient_name) + number_of_items

                # if ingredient_name does not exist in ingredients_store: +ingredient_name +number_of_items
                #
                else:
                    self.cart_map[ingredient_name] = number_of_items

    # on top:
    # if number_of_items is negative then subtracting if only the
    #
    def subtract(self, ingredient_name, number_of_items=1):

        if ingredient_name in self.cart_map.keys() and number_of_items > self.cart_map.get(ingredient_name):
            self.cart_map[ingredient_name] = self.cart_map.get(ingredient_name) - number_of_items

        if ingredient_name in self.cart_map.keys() and number_of_items == self.cart_map.get(ingredient_name):
            del self.cart_map[ingredient_name]

    # calculate total for the shopping cart
    #
    def get_total(self, discount_list=[]):   # discount_list empty by default

        # final total value (0 is default)
        #
        summary = 0

        # for each ingredient in cart:
        # if ingredient exists in discounts then adding to 'final total' the price with applied discount
        #
        for ingredient in self.cart_map:

            # for each discountList: f(x) = x.ingredient_name
            #
            if ingredient in list(map(lambda x: x.ingredient_name, discount_list)):

                # for each discountList: f(x) = x.ingredient_name and filter by ingredient_name
                # calculate_line_total for ingredient in cart_map with quantity
                # taking 1st element [0]
                #
                summary += list(filter(lambda x: x.ingredient_name == ingredient, discount_list))[0]\
                    .calculate_line_total(self.cart_map.get(ingredient), self.ingredients_store.get_ingredient_price(ingredient))

            # if no discounts available - then simply calculating price * quantity
            #
            else:
                summary += self.cart_map.get(ingredient) * self.ingredients_store.get_ingredient_price(ingredient)

        return summary

