"""Module defining the CartePizzeria class.
"""

from typing import List


class CartePizzeriaException(Exception):
    """Exception dedicated to CartePizzeria."""

    pass


class CartePizzeria:
    """Class CartePizzeria"""

    def __init__(self):
        """ """
        self.pizzas: List["Pizza"] = []

    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza: "Pizza"):
        """Add a new pizza"""
        self.pizzas.append(pizza)

    def remove_pizza(self, pizza):
        """Remove a pizza"""
        try:
            self.pizzas.remove(pizza)
        except ValueError:
            raise CartePizzeriaException(f"{pizza} was not found.")
