from gapbot.ext import BaseClient


class SetGameData(BaseClient):
    def set_game_data(self, chat_id, data_type, data, force=False):
        return self._send(
            method='gameData',
            data={
                'chat_id': chat_id,
                'type': data_type,
                'data': data,
                'force': force,
            }
        )
