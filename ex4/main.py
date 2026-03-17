from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """Play Card."""
    print("\n=== DataDeck Tournament Platform ===\n")
    try:
        card: dict = {
            "dragon": {"name": "Fire Dragon", "cost": 5,
                       "rarity": "legendry", "damage": 9, "health": 5,
                       "rating": 1200},
            "wizard": {"name": "Ice Wizard", "cost": 4, "rarity": "common",
                       "damage": 7, "health": 5, "rating": 1150}
        }
        platform = TournamentPlatform()

        dragon = TournamentCard(**card["dragon"])
        dragon.card_id = platform.register_card(dragon)
        print(f"{dragon.name} (ID: {dragon.card_id})\n"
              f"- Interfaces: "
              f"{[f"{c.__name__}" for c in type(dragon).__bases__]}"
              f"\n- Rating: {dragon.rating}\n"
              f"- Record: {dragon.win}-{dragon.lose}")
        print("")
        wizard = TournamentCard(**card["wizard"])
        wizard.card_id = platform.register_card(wizard)
        print(f"{wizard.name} (ID: {wizard.card_id})\n"
              f"- Interfaces: "
              f"{[f"{c.__name__}" for c in type(wizard).__bases__]}"
              f"\n- Rating: {wizard.rating}\n"
              f"- Record: {wizard.win}-{wizard.lose}")

        print("\nCreating tournament match...")
        print(platform.create_match(dragon.card_id, wizard.card_id))

        print("\nTournament Leaderboard:")
        card_list: list[TournamentCard] = platform.get_leaderboard()
        rating_list: list[str] = [f"{card.name} - Rating: {card.rating} "
                                  f"({card.win}-{card.lose})"
                                  for card in card_list]
        i: int = 1
        for rating in rating_list:
            print(f"{i}. {rating}")
            i += 1

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===\n"
              "All abstract patterns working together harmoniously!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
