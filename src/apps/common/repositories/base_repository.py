from abc import ABC, abstractmethod
from typing import Any, TypeVar

T = TypeVar("T")


class BaseRepository(ABC):
    """
    Base repository class for all repositories.
    """

    @abstractmethod
    def save(self, instance: T) -> T:
        """Save the instance to the database."""
        pass

    @abstractmethod
    def create(self, **kwargs: dict[str, Any]) -> T:
        """Create a new instance of the model."""
        pass

    @abstractmethod
    def get(self, **kwargs: dict[str, Any]) -> T | None:
        """Get an instance of the model by the given kwargs."""
        pass

    @abstractmethod
    def all(self) -> list[T]:
        """Get all instances of the model."""
        pass

    @abstractmethod
    def filter(self, **kwargs: dict[str, Any]) -> list[T]:
        """Get all instances of the model by the given kwargs."""
        pass

    @abstractmethod
    def delete(self, instance: T) -> None:
        """Delete the instance from the database."""
        pass

    @abstractmethod
    def update(self, instance: T, **kwargs: dict[str, Any]) -> T:
        """Update the instance with the given kwargs."""
        pass

    @abstractmethod
    def get_or_create(self, **kwargs: dict[str, Any]) -> tuple[T, bool]:
        """Get an instance of the model by the given kwargs or create a new one."""
        pass

    @abstractmethod
    def bulk_create(self, instances: list[T]) -> list[T]:
        """Create multiple instances of the model."""
        pass

    @abstractmethod
    def bulk_update(self, instances: list[T], fields: list[str]) -> list[T]:
        """Update multiple instances of the model."""
        pass

    @abstractmethod
    def set_password(self, user: T, password: str) -> None:
        """Set the password for the user."""
        pass
