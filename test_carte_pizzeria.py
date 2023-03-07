from mock import Mock

from carte_pizzeria import CartePizzeria, CartePizzeriaException


def test_carte_pizzeria_is_empty():
    """Test that an empty CartePizzeria is empty"""

    cp = CartePizzeria()

    assert cp.is_empty()


def test_carte_pizzeria_is_not_empty():
    """Test that an empty CartePizzeria is empty"""

    pizza = Mock()
    cp = CartePizzeria()
    cp.pizzas = [pizza]

    assert not cp.is_empty()


def test_carte_pizzeria_nb_pizzas():
    """Test that the number of pizzas composing a CartePizzeria
    is correct.
    """

    pizza = Mock()
    cp = CartePizzeria()
    assert cp.nb_pizzas() == 0

    cp.pizzas = [pizza, pizza]
    assert cp.nb_pizzas() == 2


def test_carte_pizzeria_add_pizza():
    """Test adding a pizza in a CartePizzeria."""

    pizza = Mock()
    cp = CartePizzeria()
    cp.add_pizza(pizza)

    assert cp.pizzas == [pizza]


def test_remove_pizza_success():
    """Test removing a pizza from a CartePizzeria."""

    pizza = Mock()
    cp = CartePizzeria()
    cp.pizzas = [pizza]

    cp.remove_pizza(pizza)
    assert cp.pizzas == []


def test_remove_pizza_failure():
    """Test removing an unknwon pizza from a CartePizzeria."""

    pizza = Mock()
    other_pizza = Mock()
    cp = CartePizzeria()
    cp.pizzas = [pizza]

    try:
        cp.remove_pizza(other_pizza)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("expected Exception was not raised")
