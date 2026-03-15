from abc import ABC, abstractmethod


class Magical(ABC):
    """Class Magical."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast spell."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Get channel mana."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """get magic stats."""
        pass
