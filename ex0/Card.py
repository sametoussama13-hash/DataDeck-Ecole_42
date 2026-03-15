"""Class card."""
from abc import ABC, abstractmethod
from enum import Enum


class CardType(Enum):
    """Class enum."""
    CREATURE = "creature"
    SPELL = "spell"
    ARTIFACT = "artifact"


class Rarity(Enum):
    LEGENDARY = "Legendary"
    COMMON = "Common"
    RARE = "Rare"
    UNCOMMON = "Uncommon"


class Card(ABC):
    """Class card."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Init base card."""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play Card."""
        pass

    def get_card_info(self) -> dict:
        """Get card info."""
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        """Check player."""
        if available_mana >= self.cost:
            return True
        else:
            return False
