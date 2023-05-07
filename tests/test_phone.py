from src.item import Item
from src.phone import Phone


def test_add_():
    item1 = Item('Ноутбук}', 50_000, 15)
    item2 = Item('Кофеварка', 5_000, 20)
    assert item1 + item2 == 35


phone = Phone("iPhone 12", 60_000, 10, 1)


def test___str__():
    assert str(phone) == 'iPhone 12'


def test___repr__():
    assert repr(phone) == "Phone('iPhone 12', 60000, 10, 1)"


def test_number_of_sim():
    assert phone.number_of_sim == 1
