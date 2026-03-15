from ex0.Card import Rarity
from ex2.EliteCard import EliteCard
from typing import Any


def main() -> None:
    """Teste Magical and Combatable Card."""
    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print(" Card: [play’, ’get_card_info’, ’is_playable’]")
    print("- Combatable: [’attack’, ’defend’, ’get_combat_stats’]")
    print("- Magical: [’cast_spell’, ’channel_mana’, ’get_magic_stats’]")
    try:
        card = EliteCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

        print("\nPlaying Arcane Warrior (Elite Card):")
        print("\nCombat phase:")
        print(f"Attack result: {card.attack("Enemy")}")
        print(f"Defense result: {card.defend(2)}")

        print("\nMagic phase:")
        targets: list[Any] = ["Enemy1", "Enemy2"]
        print(f"Spell cast: {card.cast_spell("Firball", targets)}")
        print(f"Mana channel: {card.channel_mana(3)}")

        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
