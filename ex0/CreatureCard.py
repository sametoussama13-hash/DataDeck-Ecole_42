"""Class creature card."""
from ex0.Card import Card, CardType


class CreatureCard(Card):
    """Class Creature Card."""

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        """Init base card."""
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.card_type = CardType.CREATURE

    def play(self, game_state: dict) -> dict:
        """Play Card."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def get_card_info(self) -> dict:
        """Get card info."""
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = 10
        info["health"] = 20
        return info

    def attack_target(self, target) -> dict:
        """Get card info."""
        return {"attacker": self.name, "target": target,
                "damage_dealt": self.attack, "combat_resolved": True}
