from typing import Any, Generic

from apps.common.types import DjangoModelType

# from django.db.models import Model


class BaseRepository(Generic[DjangoModelType]):
    def __init__(self, model: type[DjangoModelType]) -> None:
        self.model = model

    def save(self, instance: DjangoModelType) -> DjangoModelType:
        instance.save()
        return instance

    def create(self, **kwargs: dict[str, Any]) -> DjangoModelType:
        return self.model.objects.create(**kwargs)

    def get(self, **kwargs: dict[str, Any]) -> DjangoModelType | None:
        try:
            return self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def get_by_id(self, id: int) -> DjangoModelType | None:
        return self.get(id=id)

    def get_by_public_id(self, public_id: str) -> DjangoModelType | None:
        return self.get(public_id=public_id)
    
    def get_all(self) -> list[DjangoModelType]:
        return self.model.objects.all()
    
    def filter(self, **kwargs: dict[str, Any]) -> list[DjangoModelType]:
        return self.model.objects.filter(**kwargs)

