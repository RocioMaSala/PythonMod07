from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__ (self, name: str, creature: str):
        self._name = name
        self._type = creature
    
    @abstractmethod
    def attack(self):
        pass
    
    def describe(self) -> str:
        return(print(f"{self._name} uses a {self._type} Creature"))
    

class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", creature="Fire")
    
    def attack (self) -> str:
        return(print(f"{self._name} uses Ember!"))
    
class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", creature="Fire/Flying")

    def attack (self) -> str:
        return(print(f"{self._name} uses Flamethrower!"))
    
class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", creature="Water")

    def attack (self) -> str:
        return(print(f"{self._name} uses Water Gun!"))

class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", creature="Water")

    def attack (self) -> str:
        return(print(f"{self._name} uses Hydro Pump!"))


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str):
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Sproutling", creature="Grass")

    def attack (self):
        return(print(f"{self._name} uses Vine Whip!"))
    
    def heal (self, target = 5):
        if target < 4:
            print(f"{self._name} heals itself for a small amount")
        else:
            print(f"{self._name} doesn't heal itself for a large amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__(name="Bloomelle", creature="Grass/Fairy")

    def attack (self):
        return(print(f"{self._name} uses Petal Dance!"))
    
    def heal (self, target = 5):
        if target > 4:
            print(f"{self._name} heals itself and others for a large amount")
        else:
            print(f"{self._name} doesn't heal itself for a small amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__(name="Shiftling", creature="Normal")
        self._transformed = False

    def attack (self):
        if self._transformed == False:
            return(print(f"{self._name} attacks normally."))
        else:
            print(f"{self._name} performes a boosted strike")
    
    def transform(self):
        if self._transformed == False:
            self._transformed = True
            print(f"{self._name} shifts into a sharper form!")
    
    def revert(self):
        if self._transformed == True:
            self._transformed = False
            print(f"{self._name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__(name="Morphagon", creature="Normal/Dragon")
        self._transformed = False

    def attack (self):
        if self._transformed == False:
            return(print(f"{self._name} attacks normally."))
        else:
            print(f"{self._name} unleashes a devastating morph strike!")
    
    def transform(self):
        if self._transformed == False:
            self._transformed = True
            print(f"{self._name} morphs into a dragonic battle form!")
    
    def revert(self):
        if self._transformed == True:
            self._transformed = False
            print(f"{self._name} stabilizes its form.")






