from config.env import DjangoEnvironment, env

DJANGO_ENVIRONMENT = env.str("DJANGO_ENVIRONMENT", DjangoEnvironment.LOCAL)


if DJANGO_ENVIRONMENT == DjangoEnvironment.PRODUCTION:
    from config.settings.production import *  # noqa: F403
elif DJANGO_ENVIRONMENT == DjangoEnvironment.TESTING:
    from config.settings.testing import *  # noqa: F403
else:
    from config.settings.local import *  # noqa: F403
