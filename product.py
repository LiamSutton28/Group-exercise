"""
CP1404 Seminar task
Create a product class
"""


class Product:
    """Class for storing detail of a product"""

    def __init__(self, name="", price=0):
        """Initialise a product"""
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of a product"""
        return f"{self.name} : ${self.price:,.2f}"
