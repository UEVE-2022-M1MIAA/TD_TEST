"""Module defining unit tests of the class CartePizzeria.
"""

from mock import Mock

from carte_pizzeria import CartePizzeria, CartePizzeriaException


def test_carte_pizzeria_is_empty():
    """Test that an empty CartePizzeria is empty"""

    carte_pizzeria = CartePizzeria()

    assert carte_pizzeria.is_empty()


def test_carte_pizzeria_is_not_empty():
    """Test that an empty CartePizzeria is empty"""

    pizza = Mock()
    carte_pizzeria = CartePizzeria()
    carte_pizzeria.pizzas = [pizza]

    assert not carte_pizzeria.is_empty()


def test_carte_pizzeria_nb_pizzas():
    """Test that the number of pizzas composing a CartePizzeria
    is correct.
    """

    pizza = Mock()
    carte_pizzeria = CartePizzeria()
    assert carte_pizzeria.nb_pizzas() == 0

    carte_pizzeria.pizzas = [pizza, pizza]
    assert carte_pizzeria.nb_pizzas() == 2


def test_carte_pizzeria_add_pizza():
    """Test adding a pizza in a CartePizzeria."""

    pizza = Mock()
    carte_pizzeria = CartePizzeria()
    carte_pizzeria.add_pizza(pizza)

    assert carte_pizzeria.pizzas == [pizza]


def test_remove_pizza_success():
    """Test removing a pizza from a CartePizzeria."""

    pizza = Mock()
    carte_pizzeria = CartePizzeria()
    carte_pizzeria.pizzas = [pizza]

    carte_pizzeria.remove_pizza(pizza)
    assert not carte_pizzeria.pizzas


def test_remove_pizza_failure():
    """Test removing an unknwon pizza from a CartePizzeria."""

    pizza = Mock()
    other_pizza = Mock()
    carte_pizzeria = CartePizzeria()
    carte_pizzeria.pizzas = [pizza]

    try:
        carte_pizzeria.remove_pizza(other_pizza)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("expected Exception was not raised")
