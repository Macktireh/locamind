from abc import ABC, abstractmethod
from collections.abc import Iterable, MutableMapping, Sequence
from typing import Any, TypeVar

T = TypeVar("T")


class AbstractBaseRepository(ABC):
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
    def get_all(self) -> list[T]:
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
    def update(self, instance: T, data: dict[str, Any]) -> T:
        """Update the instance with the given kwargs."""
        pass

    @abstractmethod
    def get_or_create(
        self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: dict[str, Any]
    ) -> tuple[T, bool]:
        """Get an instance of the model by the given kwargs or create a new one."""
        pass

    @abstractmethod
    def update_or_create(
        self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: dict[str, Any]
    ) -> tuple[T, bool]:
        """Get an instance of the model by the given kwargs or create a new one."""
        pass

    @abstractmethod
    def bulk_create(
        self,
        objs: Iterable[T],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool | None = ...,
        update_fields: Sequence[str] | None = ...,
        unique_fields: Sequence[str] | None = ...,
    ) -> list[T]:
        """Create multiple instances of the model."""
        pass

    @abstractmethod
    def bulk_update(self, objs: Iterable[T], fields: Sequence[str], batch_size: int | None = ...) -> int:
        """Update multiple instances of the model."""
        pass
