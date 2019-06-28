from flask import request, jsonify
from json import dumps
from GapBot.ext import BaseClient
from .methods import Methods
from GapBot import __version__


class Gap(Methods, BaseClient):
    """GapBot, the main means for interacting with Gap Messenger Bot.

    :param host (``str``, *optional*):
        The hostname to listen on. Defaults to ``'0.0.0.0'``  to have the server available externally as well.
        This parameter will be used to get a update from Gap server with Flask.

    :param callback (``str``, *optional*):
        The second part of url after domain. Set as webhook on Gap Developer Panel. Default to  ``'/webhook'``.
        This parameter will be used to get a update from Gap server with Flask.

    :param port (``int``, *optional*):
        The port of the webserver. Defaults to ``5000``.
        This parameter will be used to get a update from Gap server with Flask.


    :param bot_token (``str``, *optional*):
        Pass your Bot API token to use Gap api methods.
        This parameter will be used to methods from Gap api with requests.
    """

    def __init__(self,
                 host: str = '0.0.0.0',
                 callback: str = '/webhook',
                 port: int = 5000,
                 bot_token: str = None
                 ):
        super().__init__()
        self.host = host
        self.port = port
        self.callback = callback
        self.bot_token = bot_token
        self.handler = None

    def run(self):
        @self.flask_app.route('/info', methods=['POST', 'GET', 'PUT'])
        def gapbot_info():
            result = {
                'Module': 'GapBot',
                'APP_VERSION': __version__,
            }
            return jsonify(result)

        @self.flask_app.route(self.callback, methods=['POST'])
        def webhook():
            self.handler(self, dict(request.form))
            return dumps(request.form)
        self.flask_app.run(host=self.host, port=self.port, debug=False)
