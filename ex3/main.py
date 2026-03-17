from ex0.Card import Card
from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    """Test ex3."""
    print("\n=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...\n")
    try:
        factory = FantasyCardFactory()
        print(f"Factory: {(FantasyCardFactory).__name__}")

        strategy = AggressiveStrategy()
        print(f"Strategy: {(AggressiveStrategy).__name__}")

        type_card: list[FantasyCardFactory] = [factory.create_creature,
                                               factory.create_artifact,
                                               factory.create_spell]

        input_type: list[str] = ["dragon", "goblin", "fireball", "mana_ring"]
        for input_name in input_type:
            for type_c in type_card:
                card_h = type_c(input_name)
                if isinstance(card_h, Card):
                    break

        print(f"Available types: {factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        game = GameEngine()
        game.configure_engine(factory, strategy)
        turn = game.simulate_turn()
        print("\nTurn execution:")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Actions: {turn}")

        print(f"\nGame Report:\n{game.get_engine_status()}")

        print("\nAbstract Factory + Strategy Pattern: "
              "Maximum flexibility achieved!\n")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
