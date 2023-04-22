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
