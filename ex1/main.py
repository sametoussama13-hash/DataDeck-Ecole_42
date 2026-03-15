from ex0.Card import CardType
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from typing import Any


def main() -> None:
    """Lunch a Data Deck."""
    print("\n=== DataDeck Deck Builder ===")
    try:
        creaturecard: dict[Any] = {
            CreatureCard: {"name": "Fire Dragon", "cost": 5,
                           "rarity": "Legendary",
                           "attack": 7, "health": 5},
            ArtifactCard: {"name": "Mana Crystal", "cost": 2,
                           "rarity": "Common",
                           "durability": 5,
                           "effect": "Permanent: +1 mana per turn"},
            SpellCard: {"name": "Lightning Bolt", "cost": 3,
                        "rarity": "Common",
                        "effect_type": "Deal 3 damage to target’"}
        }

        print("\nBuilding deck with different card types...")
        deck = Deck()
        print(CardType.CREATURE)
        for cls, value in creaturecard.items():
            card = cls(**value)
            deck.add_card(card)
        deck.shuffle()
        print(f"Deck stats: {deck.get_deck_stats()}")

        print("\nDrawing and playing cards:")

        i: int = len(deck.card_list)
        while i > 0:
            drew = deck.draw_card()
            print(f"\nDrew: {drew.name}")
            print(f"Play result: {drew.play({})}")
            i -= 1

        print("\nPolymorphism in action: Same interface,"
              "different card behaviors!\n")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
