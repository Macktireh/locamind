from enum import Enum
from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DjangoEnvironment(str, Enum):
    LOCAL = "local"
    TESTING = "testing"
    PRODUCTION = "production"


def env_to_enum(enum_cls: DjangoEnvironment, value: str) -> str:
    for x in enum_cls:
        if x.value == value:
            return x

    raise ImproperlyConfigured(f"Env value {repr(value)} could not be found in {repr(enum_cls)}")
