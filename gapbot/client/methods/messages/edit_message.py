from gapbot.ext import BaseClient
from json import dumps


class EditMessage(BaseClient):
    def edit_message(self, chat_id, message_id, new_text, inline_keyboard=None):
        return self._send(
            method='editMessage',
            data={
                'chat_id': chat_id,
                'message_id': message_id,
                'data': new_text,
                'inline_keyboard': dumps(inline_keyboard) if inline_keyboard else None,
            }
        )
