# Setting up a new class.

class Shirt:
    """
        Create new instances of shirt objects
    """

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.stroke = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        # set a new price for the shirt property
        self.price = new_price

    def discount(self, discount_value):
        return self.price *(1 - discount_value)
