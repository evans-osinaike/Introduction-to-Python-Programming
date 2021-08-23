class Pants:
    """
        create new instance of the pants objects.
    """

    def __init__(self, pant_color, pant_waist_size, pant_length, pant_price):
        self.color = pant_color
        self.waist_size = pant_waist_size
        self.length = pant_length
        self.price = pant_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount_value):
        return self.price * (1 - discount_value)
