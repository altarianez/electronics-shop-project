"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    phone = Item("Айфон", 70000, 20)
    assert phone.calculate_total_price() == 1400000


def test_apply_discount():
    phone = Item("Айфон", 50000, 15)
    assert phone.pay_rate == 1.0

    Item.pay_rate = 0.8
    phone.apply_discount()
    assert phone.pay_rate == 0.8
    assert phone.price == 40000


def test_item_generation():
    phone = Item("Айфон", 50000, 30)
    assert phone.name == "Айфон"
    assert phone.price == 50000
    assert phone.quantity == 30


def test_name_setter():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    with pytest.raises(ValueError):
        Item('СуперСмартфонище', 100000, 10)


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].name == "Ноутбук"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add_():
    item1 = Item('Ноутбук}', 50_000, 15)
    item2 = Item('Кофеварка', 5_000, 20)
    assert item1 + item2 == 35
