from ex1.factory_creation_creature_ex1 import TransformCreatureFactory
from ex1.factory_creation_creature_ex1 import HealingCreatureFactory


if __name__ == "__main__":

    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()
    print(" base:")
    healing_factory_base = healing_factory.create_base()
    healing_factory_base.describe()
    healing_factory_base.attack()
    healing_factory_base.heal()  # type: ignore

    print(" evolved:")
    healing_factory_evolved = healing_factory.create_evolved()
    healing_factory_evolved.describe()
    healing_factory_evolved.attack()
    healing_factory_evolved.heal()  # type: ignore

    print("\n")
    print("Testing Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    print(" base:")
    transform_factory_base = transform_factory.create_base()
    transform_factory_base.describe()
    transform_factory_base.attack()
    transform_factory_base.transform()  # type: ignore
    transform_factory_base.attack()
    transform_factory_base.revert()  # type: ignore

    print(" evolved:")
    transform_factory_evolved = transform_factory.create_evolved()
    transform_factory_evolved.describe()
    transform_factory_evolved.attack()
    transform_factory_evolved.transform()  # type: ignore
    transform_factory_evolved.attack()
    transform_factory_evolved.revert()  # type: ignore
