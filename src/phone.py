from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value_: int) -> None:
        if value_ <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = value_
