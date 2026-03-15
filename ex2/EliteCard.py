from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Magical, Combatable):
    """Class ElitCard."""

    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, health: int,) -> None:
        """Build Elit card."""
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.attacked = "melee"
        self.total_mana = cost

    def play(self, game_state: dict) -> dict:
        """Play Card."""
        return {"card_player": self.name, "mana_used": self.cost,
                "effect": self.attacked}

    def get_card_info(self) -> dict:
        """Get card info."""
        return {"cerard_play": self.name, "mana_used": self.cost,
                "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        """Check is playable card."""
        if available_mana >= self.cost:
            return True
        return False

    def attack(self, target) -> dict:
        """Attack Combatable."""
        return {"attacker": self.name, "target": target,
                "damage": self.damage, "combat_type": self.attacked}

    def defend(self, incoming_damage: int) -> dict:
        """Defend Combatable."""
        if self.health > self.health:
            b: bool = False
        else:
            b: bool = True
        return {"attacker": self.name, "damage_taken": incoming_damage,
                "damage_bloqued": self.health, "still_alive": b}

    def get_combat_stats(self) -> dict:
        """Get Combatable."""
        return {"card_name": self.name,
                "damage": self.damage,
                "health": self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast Spell."""
        return {"caster": self.name, "spell": spell_name,
                "target": targets, "mana_used": self.cost}

    def channel_mana(self, amount: int) -> dict:
        """Get channel mana spell."""
        self.total_mana += amount
        return {"channeled": amount, "total_mana": self.total_mana}

    def get_magic_stats(self) -> dict:
        """get Spell stats."""
        return {"card_name": self.name,
                "start_mana": self.cost,
                "total_mana": self.total_mana}
