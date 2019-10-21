from gapbot.ext import BaseClient


class GetGameData(BaseClient):
    def get_game_data(self, chat_id, data_type):
        return self._send(
            method='gameData',
            data={
                'chat_id': chat_id,
                'type': data_type,
            }
        )
