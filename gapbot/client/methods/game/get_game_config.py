from gapbot.ext import BaseClient


class GetGameConfig(BaseClient):
    def get_game_config(self, key=None):
        return self._send(
            method='getGameConfig',
            data={
                'key': key,
            }
        )
