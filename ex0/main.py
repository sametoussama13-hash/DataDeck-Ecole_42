from ex0.CreatureCard import CreatureCard
from typing import Any


def main() -> None:
    """Test Card."""
    print("\n=== DataDeck Card Foundation ===\n")

    creaturecard: dict[Any] = {
        "name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
        "attack": 7, "health": 5
    }
    try:
        card = CreatureCard(**creaturecard)
        print(f"CreatureCard Info:\n{card.get_card_info()}")

        print("\nPlaying Fire Dragon with 6 mana available:")
        mana: int = 6
        print(f"playable: {card.is_playale(mana)}")
        print(f"Play result: {card.play({})}")

        print("\nFire Dragon attacks Goblin Warrior:")
        target: str = "Goblin Warrior"
        print(f"Attack result: {card.attack_target(target)}")

        print("\nTesting insufficient mana (3 available):")
        mana = 3
        print(f"Plalayble: {card.is_playale(mana)}")

        print("\nAbstract pattern successfully demonstrated!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
