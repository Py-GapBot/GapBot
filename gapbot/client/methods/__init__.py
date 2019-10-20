from .decorators import Decorators
from .messages import Messages
from .extra import Extra
from .callbacks import Callbacks


class Methods(Decorators, Messages, Extra, Callbacks):
    pass
