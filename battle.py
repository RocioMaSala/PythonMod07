from ex0.factory_creation_creature import FlameFactory, AquaFactory
from ex0.factory_creation_creature import CreatureFactory


def verificator(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    if base_creature is None or evolved_creature is None:
        print("The factory creation has an Error")
        return

    print("Testing Factory")
    base_creature.describe()
    base_creature.attack()
    evolved_creature.describe()
    evolved_creature.attack()
    print("\n")


def creature_fight(factoryone: CreatureFactory, factorytwo: CreatureFactory) -> None:
    
    playerone = factoryone.create_base()
    playertwo = factorytwo.create_base()
    
    playerone.describe()
    print("vs.")
    playertwo.describe()
    playerone.attack()
    playertwo.attack()


if __name__ == "__main__":

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    verificator(flame_factory)
    verificator(aqua_factory)
   
    creature_fight(flame_factory, aqua_factory)
