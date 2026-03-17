from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Class AggressiveStrategy."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Excute turn."""
        card_played: list[str] = []
        mana: int = 10
        mana_rest: int = 10
        damage: int = 0
        targets = self.prioritize_targets(battlefield)
        for card in sorted(hand, key=lambda card: card.cost):
            if card.cost <= mana:
                card_played.append(card.name)
                mana -= card.cost
                if hasattr(card, "attack"):
                    damage += card.attack
        return {"cards_played": card_played, "mana_used": (mana_rest - mana),
                "target_attacked": targets, "damage_dealt": damage}

    def get_strategy_name(self) -> str:
        """Get strategy."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Pute target."""
        return available_targets
