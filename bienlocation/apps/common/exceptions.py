class ApplicationError(Exception):
    def __init__(self, message, extra=None):
        super().__init__(message)

        self.message = message
        self.extra = extra or {}


class AccountDeactivatedError(ApplicationError):
    pass


class UserAlreadyExistsError(ApplicationError):
    pass

