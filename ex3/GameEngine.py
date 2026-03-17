from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
import random


class GameEngine:
    """Class GameEngine."""

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Configurte engine."""
        self.factory = factory
        self.strategy = strategy
        self.turns_nbr = 0

    def simulate_turn(self) -> dict:
        """Simulate turn."""
        self.deck = self.factory.create_themed_deck(9)
        deck_card: list = []
        for _, card in self.deck.items():
            deck_card.extend(card)
        self.hand: list[Card] = random.sample(deck_card, 3)
        print(f"Hand: {[f"{card.name} ({card.cost})" for card in self.hand]}")
        result_turn = self.strategy.execute_turn(self.hand, ["Enemy Player"])
        self.result_turn: dict | None = result_turn
        self.turns_nbr += 1
        return self.result_turn

    def get_engine_status(self) -> dict:
        """Get engine."""
        return {"turns_simulated": self.turns_nbr,
                "strategy_used": self.strategy.get_strategy_name(),
                "total_damage": self.result_turn["damage_dealt"],
                "cards_created": len(self.hand)}
