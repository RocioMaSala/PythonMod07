from ex0.factory_creation_creature import FlameFactory, AquaFactory
from ex1.factory_creation_creature_ex1 import TransformCreatureFactory
from ex1.factory_creation_creature_ex1 import HealingCreatureFactory
from ex2.battlestrategy import NormalStrategy, AggressiveStrategy
from ex2.battlestrategy import DefensiveStrategy
from typing import Any
from itertools import combinations


def battle(opponents: list[tuple[Any, Any]]) -> None:
    fighters = []
    display_list = []

    for factory, strategy in opponents:
        creature_instance = factory.create_base()
        fighters.append((creature_instance, strategy))
        c_name = creature_instance._name
        s_name = strategy.__class__.__name__.replace("Strategy", "")
        display_list.append(f"({c_name}+{s_name})")

    print(f"[ {', '.join(display_list)} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    try:
        pairs = combinations(fighters, 2)

        for (creature_a, strategy_a), (creature_b, strategy_b) in pairs:
            print("* Battle *")
            creature_a.describe()
            print(" vs.")
            creature_b.describe()
            print(" now fight!")

            strategy_a.act(creature_a)
            strategy_b.act(creature_b)
            print("\n")

    except Exception as e:
        print(f"Battle error, aborting torunament: {e}\n")


if __name__ == "__main__":

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle(
        [(flame_factory, normal_strategy),
         (healing_factory, defensive_strategy)]
        )

    print("Tournament 1 (error)")
    battle(
        [(flame_factory, aggressive_strategy),
         (healing_factory, defensive_strategy)]
        )

    print("Tournament 2 (multiple)")
    battle(
        [(aqua_factory, normal_strategy),
         (healing_factory, defensive_strategy),
         (transform_factory, aggressive_strategy)]
         )
