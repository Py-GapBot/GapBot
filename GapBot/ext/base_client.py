from GapBot import __version__
from flask import Flask
from re import compile


class BaseClient:
    APP_VERSION = "GapBot {}".format(__version__)
    BOT_TOKEN_RE = compile(r"^[A-Za-z0-9]{64}$")
    CALLBACK_RE = compile(r"^(http|https)?$")
    flask_app = Flask(__name__)

    def __init__(self):
        self.host = None
        self.port = None
        self.callback = None
        self.bot_token = None
        self.handler = None
