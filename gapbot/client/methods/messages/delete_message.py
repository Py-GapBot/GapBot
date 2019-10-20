from gapbot.ext import BaseClient


class DeleteMessage(BaseClient):
    def delete_message(self, chat_id, message_id):
        return self._send(
            method='deleteMessage',
            data={
                'chat_id': chat_id,
                'message_id': message_id,
            }
        )
