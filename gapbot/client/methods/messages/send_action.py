from gapbot.ext import BaseClient


class SendAction(BaseClient):
    def send_action(self, chat_id, action='typing'):
        return self._send(
            method='sendAction',
            data={
                'chat_id': chat_id,
                'type': action,
            }
        )
