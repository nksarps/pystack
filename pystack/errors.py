class PyStackError(Exception):
    """
    Base class for all exceptions raised by PyStack.
    """
    pass

class MissingSecretKeyError(PyStackError):
    """
    Raised when a secret key is missing.
    """
    pass

class InvalidMethodError(PyStackError):
    """
    Raised when an invalid request method is provided
    """
    pass