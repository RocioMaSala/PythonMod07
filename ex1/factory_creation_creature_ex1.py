from abc import ABC, abstractmethod
from .capabilities import Flameling, Pyrodon, Aquabub, Torragon, Sproutling, Bloomelle, Shiftling, Morphagon

class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass
    
    @abstractmethod
    def create_evolved(self):
        pass

class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()

class AquaFactory(CreatureFactory):
    def create_base(self):
        return Aquabub()

    def create_evolved(self):
        return Torragon()

class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()
    
    def create_evolved(self):
        return Bloomelle()
    

class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()
    
    def create_evolved(self):
        return Morphagon()
            

    

