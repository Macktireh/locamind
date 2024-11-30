from collections.abc import Iterable, MutableMapping, Sequence
from typing import Any, Generic, TypeVar, override

from django.db.models import Model
from django.db.models.manager import BaseManager

from apps.common.repositories.abstract_base_repository import AbstractBaseRepository

T = TypeVar("T", bound=Model)


class DjangoRepository(AbstractBaseRepository, Generic[T]):
    def __init__(self, model: type[T]) -> None:
        self.model = model

    @override
    def save(self, instance: T) -> T:
        self._check_instance(instance)
        instance.save()
        return instance

    @override
    def create(self, **kwargs: dict[str, Any]) -> T:
        return self.model.objects.create(**kwargs)

    @override
    def get(self, **kwargs: dict[str, Any]) -> T | None:
        return self.model.objects.get(**kwargs)

    @override
    def get_all(self) -> BaseManager[T]:
        return self.model.objects.all()

    @override
    def filter(self, **kwargs: dict[str, Any]) -> BaseManager[T]:
        return self.model.objects.filter(**kwargs)

    @override
    def delete(self, instance: T) -> None:
        self._check_instance(instance)
        instance.delete()

    @override
    def update(self, instance: T, data: dict[str, Any]) -> T:
        self._check_instance(instance)
        for key, value in data.items():
            setattr(instance, key, value)
        return self.save(instance)

    @override
    def get_or_create(
        self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: dict[str, Any]
    ) -> tuple[T, bool]:
        return self.model.objects.get_or_create(**kwargs)

    @override
    def update_or_create(
        self, defaults: MutableMapping[str, Any] | None = ..., **kwargs: dict[str, Any]
    ) -> tuple[T, bool]:
        return self.model.objects.update_or_create(**kwargs)

    @override
    def bulk_create(
        self,
        objs: Iterable[T],
        batch_size: int | None = ...,
        ignore_conflicts: bool = ...,
        update_conflicts: bool | None = ...,
        update_fields: Sequence[str] | None = ...,
        unique_fields: Sequence[str] | None = ...,
    ) -> list[T]:
        return self.model.objects.bulk_create(
            objs=objs,
            batch_size=batch_size,
            ignore_conflicts=ignore_conflicts,
            update_conflicts=update_conflicts,
            update_fields=update_fields,
            unique_fields=unique_fields,
        )

    @override
    def bulk_update(self, objs: Iterable[T], fields: Sequence[str], batch_size: int | None = ...) -> int:
        return self.model.objects.bulk_update(objs=objs, fields=fields, batch_size=batch_size)

    def _check_instance(self, instance: T) -> None:
        if not isinstance(instance, type(self.model)):
            raise TypeError(
                f"The instance must be of type {self.model_type.__name__}, but got {type(instance)}"
            )

