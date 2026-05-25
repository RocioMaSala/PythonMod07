from abc import ABC
from .creature import Flameling, Pyrodon, Aquabub, Torragon

class CreatureFactory(ABC):
    def create_base(self):
        pass
    
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
            

    

