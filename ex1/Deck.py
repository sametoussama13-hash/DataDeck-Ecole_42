"""Class Deck."""
from ex0.Card import Card, CardType
import random


class Deck:
    """Class Deck."""

    def __init__(self) -> None:
        """Init card list."""
        self.card_list: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Init Deck."""
        self.card_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Play Card."""
        for card in self.card_list:
            if card.name == card_name:
                self.card_list.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Resolve effect."""
        random.shuffle(self.card_list)

    def draw_card(self) -> Card:
        """Draw card."""
        return self.card_list.pop(0)

    def get_deck_stats(self) -> dict:
        """get deck stats."""
        stats: dict[int] = {"total_cards": 0, "creatures": 0, "spells": 0,
                            "artifacts": 0, "avg_cost": 0}
        stats["total_cards"] = len(self.card_list)
        total_cost: int = 0
        for card in self.card_list:
            total_cost += card.cost
            if card.card_type == CardType.CREATURE:
                stats["creatures"] += 1
            elif card.card_type == CardType.ARTIFACT:
                stats["artifacts"] += 1
            elif card.card_type == CardType.SPELL:
                stats["spells"] += 1
        stats["avg_cost"] = round(total_cost / len(self.card_list), 1)
        return stats
