"""Class Artifact Card."""
from ex0.Card import Card, CardType


class ArtifactCard(Card):
    """Class Artifact Card."""

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: str, effect: str) -> None:
        """Init Artifact Card."""
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.card_type = CardType.ARTIFACT

    def play(self, game_state: dict) -> dict:
        """Play Card."""
        return {"card_player": self.name, "mana_used": self.cost,
                "effect": self.effect}

    def activate_ability(self) -> dict:
        """Resolve effect."""
        return {"effect_type": self.effect,
                "resolved": True}
