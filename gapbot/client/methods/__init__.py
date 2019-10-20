from .decorators import Decorators
from .messages import Messages
from .extra import Extra
from .callbacks import Callbacks
from .payment import Payment


class Methods(Decorators, Messages, Extra, Callbacks, Payment):
    pass
