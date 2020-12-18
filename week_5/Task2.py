class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.order_number = Pizza.order_number
        Pizza.order_number += 1

    @staticmethod
    def pepperoni():
        new_ingredients = ['bacon', 'mozzarella', 'oregano']
        return Pizza(new_ingredients)

    @staticmethod
    def hawaiian():
        new_ingredients = ['ham', 'pineapple']
        return Pizza(new_ingredients)

    @staticmethod
    def margherita():
        new_ingredients = ['mozzarella', 'olives', 'tomatoes']
        return Pizza(new_ingredients)
