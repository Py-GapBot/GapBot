from gapbot.ext import BaseClient


class GetTopPlayers(BaseClient):
    def get_top_players(self, chat_id, time):
        return self._send(
            method='leaderBoard',
            data={
                'chat_id': chat_id,
                'time': time,
            }
        )
