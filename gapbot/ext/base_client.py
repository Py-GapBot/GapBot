from gapbot import __version__
from flask import Flask
from re import compile
from requests import sessions


class BaseClient:
    APP_VERSION = "gapbot {}".format(__version__)
    BOT_TOKEN_RE = compile(r"^[A-Za-z0-9]{64}$")
    CALLBACK_RE = compile(r"^(http|https)?$")
    flask_app = Flask(__name__)
    BASE_URL = 'https://api.gap.im'

    def __init__(self):
        self.host = None
        self.port = None
        self.callback = None
        self.bot_token = None
        self.handler = None
        self.session = sessions.session()

    def _send(self, *args, **kwargs):
        pass

    def upload(self, *args, **kwargs):
        pass
