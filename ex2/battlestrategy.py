from ex1.capabilities import TransformCapability, HealCapability, Creature
from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            creature.transform()  # type: ignore
            creature.attack()
            creature.revert()  # type: ignore
        else:
            creature_name = creature.__class__.__name__
            raise ValueError(
                f"Invalid Creature '{creature_name}' "
                "for this Aggressive strategy"
                )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            creature.attack()
            creature.heal()  # type: ignore
        else:
            creature_name = creature.__class__.__name__
            raise ValueError(
                f"Invalid Creature '{creature_name}' "
                "for this Defensive strategy"
                )
