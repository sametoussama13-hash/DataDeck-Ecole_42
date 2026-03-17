from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.Card import Card, CardType


class FantasyCardFactory(CardFactory):
    """Class FantasyCardFactory."""

    def __init__(self) -> None:
        """Build Card Factory."""
        self.deck: Deck = Deck()
        self.creatures: dict = {
            "dragon": {"name": "Fire Dragon",
                               "cost": 5,
                       "rarity": "Legendary",
                       "attack": 7,
                       "health": 5},
            "goblin": {"name": "Goblin Warrior",
                       "cost": 2,
                       "rarity": "Legendary",
                       "attack": 7, "health": 5}}
        self.spells: dict = {
            "fireball": {"name": "Lightning Bolt", "cost": 4,
                         "rarity": "Common",
                         "effect_type": "Deal 3 damage to target’"}}
        self.artifacts: list[dict] = {
            "mana_ring": {"name": "Mana Crystal", "cost": 2,
                          "rarity": "Common",
                          "durability": 5,
                          "effect": "Permanent: +1 mana per turn"}
            }
        self.created_card: dict[str, Card] = {
            f"{CardType.CREATURE.value}s": [],
            f"{CardType.SPELL.value}s": [],
            f"{CardType.ARTIFACT.value}s": []}
        self.card_created: list[Card] = []

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create Creature."""
        for name, value in self.creatures.items():
            if name == name_or_power:
                card = CreatureCard(**value)
                self.card_created.append(card)
                list_c: list = self.created_card[f"{CardType.CREATURE.value}s"]
                list_c.append(card)
                return card
        return name_or_power

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create Spell."""
        for name, value in self.spells.items():
            if name == name_or_power:
                card = SpellCard(**value)
                self.card_created.append(card)
                list_c: list = self.created_card[f"{CardType.SPELL.value}s"]
                list_c.append(card)
                return card
        return name_or_power

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create Artifact."""
        for name, value in self.artifacts.items():
            if name == name_or_power:
                card = ArtifactCard(**value)
                self.card_created.append(card)
                list_c: list = self.created_card[f"{CardType.ARTIFACT.value}s"]
                list_c.append(card)
                return card
        return name_or_power

    def create_themed_deck(self, size: int) -> dict:
        """Create themed deck."""
        type_method: list[FantasyCardFactory] = [self.create_creature,
                                                 self.create_artifact,
                                                 self.create_spell]
        type_card: list[str] = []
        for _, value in self.created_card.items():
            type_card.extend(value)
        for i in range(size):
            d = i % len(type_card)
            for type_ in type_method:
                card = type_(type_card[d])
                if isinstance(card, Card):
                    self.deck.add_card(card)
                    break
        return self.created_card

    def get_supported_types(self) -> dict:
        """Get supported types."""
        return {
            f"{CardType.CREATURE.value}s": ["dragon", "goblin"],
            f"{CardType.SPELL.value}s": ["fireball"],
            f"{CardType.ARTIFACT.value}s": ["mana_ring"]}
