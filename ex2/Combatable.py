from abc import ABC, abstractmethod


class Combatable(ABC):
    """Clas Combatable."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Atack methode."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend methode."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Get combat."""
        pass
