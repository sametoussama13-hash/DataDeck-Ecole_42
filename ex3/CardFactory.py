from ex0.Card import Card
from abc import ABC, abstractmethod


class CardFactory(ABC):
    """Class  CardFactory."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create Creature"""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create Spell."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create Artifact."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create themed deck."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Get supported types."""
        pass
