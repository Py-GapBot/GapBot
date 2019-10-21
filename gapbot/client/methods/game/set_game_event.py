from gapbot.ext import BaseClient


class SetGameEvent(BaseClient):
    def set_game_event(self, event, value=None):
        return self._send(
            method='gameEvent',
            data={
                'event': event,
                'value': value,
            }
        )
