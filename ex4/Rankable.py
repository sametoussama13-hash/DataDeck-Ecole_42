from abc import ABC, abstractmethod


class Rankable(ABC):
    """Class Rankable."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update wins."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update losses."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Get rank info."""
        pass
