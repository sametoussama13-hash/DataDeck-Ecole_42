from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Class TournamentPlatform."""

    def __init__(self) -> None:
        self.status: str = "active"
        self.card_register: dict = {}
        self.list_card: list[TournamentCard] = []
        self.match_played: int = 0
        self.dragon_count: int = 0
        self.wizard_count: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register card."""
        card_available: dict[str, TournamentCard] = {
            "Fire Dragon": self.dragon_count,
            "Ice Wizard": self.wizard_count}
        for name, count in card_available.items():
            if card.name == name:
                count += 1
                card.card_id = f"{name.split(" ", 1)[1]}_{count:03d}".lower()
                self.list_card.append(card)
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Create match."""
        list_match: list[TournamentCard] = []
        for card in self.list_card:
            if card.card_id == card1_id or card.card_id == card2_id:
                list_match.append(card)
        list_match.sort(key=lambda card: card.power, reverse=True)
        self.winner, self.loser = list_match
        self.winner.update_wins(1)
        self.loser.update_losses(1)
        for card in list_match:
            card.calculate_rating()
        self.match_played += 1
        return {"winner": self.winner.card_id, "loser": self.loser.card_id,
                "winner_rating": self.winner.rating,
                "loser_rating": self.loser.rating}

    def get_leaderboard(self) -> list:
        """Get leadrbord."""
        self.list_card.sort(key=lambda card: card.rating, reverse=True)
        return self.list_card

    def generate_tournament_report(self) -> dict:
        """Generate tournament report."""
        total_rating: int = sum(card.rating for card in self.list_card)
        avg_rating: int = (total_rating / len(self.list_card))
        return {"totals_cards": len(self.list_card),
                "matches_played": self.match_played,
                "avg_rating": int(avg_rating), "platform_status": self.status}
