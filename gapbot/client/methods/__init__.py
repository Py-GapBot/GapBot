from .decorators import Decorators
from .messages import Messages
from .extra import Extra
from .callbacks import Callbacks
from .payment import Payment
from .game import Game


class Methods(Decorators, Messages, Extra, Callbacks, Payment, Game):
    pass
