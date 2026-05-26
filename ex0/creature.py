from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature: str) -> None:
        self._name = name
        self._type = creature

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> None:
        print(f"{self._name} uses a {self._type} Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", creature="Fire")

    def attack(self) -> None:
        print(f"{self._name} uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", creature="Fire/Flying")

    def attack(self) -> None:
        print(f"{self._name} uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", creature="Water")

    def attack(self) -> None:
        print(f"{self._name} uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", creature="Water")

    def attack(self) -> None:
        print(f"{self._name} uses Hydro Pump!")
