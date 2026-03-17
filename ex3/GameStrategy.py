from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Class  GameStrategy."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Excute."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Get strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Pute target."""
        pass
