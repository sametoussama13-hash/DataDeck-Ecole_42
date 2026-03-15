"""Class Spell Card."""
from ex0.Card import Card, CardType


class SpellCard(Card):
    """class Spell Card."""

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        """Init Spelle Card."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.card_type = CardType.SPELL

    def play(self, game_state: dict) -> dict:
        """Play Card."""
        return {"card_player": self.name, "mana_used": self.cost,
                "effect": self.effect_type}

    def resolve_effect(self, targets: list) -> dict:
        """Resolve effect."""
        return {"effect_type": self.effect_type,
                "targets": targets,
                "resolved": True}
