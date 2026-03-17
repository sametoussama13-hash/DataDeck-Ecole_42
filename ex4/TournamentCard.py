from ex2.Combatable import Combatable
from ex0.Card import Card
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Class TournamentCard."""

    def __init__(self, name, cost, rarity, damage, health, rating) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = None
        self.lose = 0
        self.win = 0
        self.power = damage
        self.health = health
        self.rating = rating

    # """Methode Rankable"""
    def calculate_rating(self) -> int:
        """Calculate rating."""
        self.rating = (self.rating + (self.win * 16) - (self.lose * 16))
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Update wins."""
        self.win += wins
        return self.win

    def update_losses(self, losses: int) -> None:
        """Update losses."""
        self.lose += losses
        return self.lose

    def get_rank_info(self) -> dict:
        """Get rank info."""
        return {"name": self.name,
                "rating": self.rating,
                "wins": self.win,
                "lose": self.lose,
                "record": f"{self.win}-{self.lose}"}

    # """Methode Card."""
    def play(self, game_state: dict) -> dict:
        """Play."""
        return {
            "card_played": self.name,
            "mana_used": self.cost}

    # """Methode Combatable."""
    def attack(self, target) -> dict:
        """Atack methode."""
        return {"attacker": self.name, "target": target,
                "damage": self.power, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> dict:
        """Defend methode."""
        if incoming_damage > self.health:
            b: bool = False
        else:
            b: bool = True
        return {"attacker": self.name, "damage_taken": incoming_damage,
                "damage_bloqued": self.health, "still_alive": b}

    def get_combat_stats(self) -> dict:
        """Get combat."""
        return {"card_name": self.name,
                "damage": self.power,
                "health": self.health}

    # """Methode TournamentCard."""
    def get_tournament_stats(self) -> dict:
        """Get tournament_status."""
        return {"name": self.name,
                "rating": self.rating,
                "wins": self.win,
                "lose": self.lose,
                "record": f"{self.win}-{self.lose}",
                "attack": self.power,
                "health": self.health}
