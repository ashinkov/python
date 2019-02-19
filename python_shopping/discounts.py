'''
python: Discount module

by Alexander Shinkov (@ashinkov)

TODO:
Discount classes inherit from AbstractDiscount and must implement the calculate_line_total() method.

Two discount classes are provided; NoDiscount, BulkDiscount.

NoDiscount:
No discount is applied and the price remains unaffected.
tomatoes_nodiscount = NoDiscount('tomatoes')

BulkDiscount:
A discount that applies when you buy a specific quantity. For example, buy one get one free, or, buy two get a third free.

buy one get one free on tomatoes
buy_one_get_one_free_tomatoes = BulkDiscount('tomatoes', 1, 1)

buy two get third free on onions
buy_two_get_third_free_onions = BulkDiscount('onions', 2, 1)

'''

from abc import ABC, abstractmethod


class AbstractDiscount(ABC):

    # for all children to implement calculate_line_total
    #
    @abstractmethod
    def calculate_line_total(self, quantity, price):
        pass


# 1st case NoDiscount: following the logic:
# we have no discount for ingredient_name: returning quantity * price in this case)
#
class NoDiscount(AbstractDiscount):

    def __init__(self, ingredient_name):
        self.ingredient_name = ingredient_name

    def calculate_line_total(self, quantity, price):
        return quantity * price


'''
2nd case is BulkDiscount: following the logic:

A discount that applies when you buy a specific quantity.

For example, buy one get one free, or, buy two get a third free.

cases:
------
1) ---> buy one get one free on tomatoes
buy_one_get_one_free_tomatoes = BulkDiscount('tomatoes', 1, 1)
2) ---> buy two get third free on onions
buy_two_get_third_free_onions = BulkDiscount('onions', 2, 1)

required quantity / need to buy quantity
1 / 1
2 / 2
3 / 2
4 / 3
5 / 4
6 / 4
7 / 5
8 / 6
9 / 6
'''

class BulkDiscount(AbstractDiscount):

    # triggers discount calculation
    # get_quantity  -> how many items we need to buy for discount to be triggered
    # free_quantity -> how many items we would get for free when discount is triggered
    #
    def __init__(self, ingredient_name, get_quantity, free_quantity):
        self.ingredient_name = ingredient_name
        self.get_quantity = get_quantity
        self.free_quantity = free_quantity

    # final price calculation after applying discount for each case of discount
    #
    def calculate_line_total(self, quantity, price):

        # default discount_quantity = 0
        #
        discount_quantity = 0

        # initial counter value
        #
        j = 0

        # from 0 to quantity: when j=get_quantity -> then adding free_quantity and setting j back to 0 to initial value
        #
        for i in range(0, quantity, 1):

            # if counter = get_quantity to get discount then +free_quantity
            #
            if j == self.get_quantity:
                discount_quantity = discount_quantity + self.free_quantity
                j = 0

            # adding +1 to j to get discount if counter <> get_quantity to get discount
            #
            else:
                j += 1

        # getting the final price after BulkDiscount applied
        #
        return (quantity - discount_quantity) * price



