from gapbot.ext import BaseClient
from json import dumps


class SendVoice(BaseClient):
    def send_voice(self, chat_id, path, caption=None, reply_keyboard=None, inline_keyboard=None, reply_form=None):
        return self._send(
            method='sendMessage',
            data={
                'chat_id': chat_id,
                'type': 'voice',
                'data': self.upload(chat_id=chat_id, file_type='voice', path=path, desc=caption),
                'reply_keyboard': dumps(reply_keyboard) if reply_keyboard else None,
                'inline_keyboard': dumps(inline_keyboard) if inline_keyboard else None,
                'form': dumps(reply_form) if reply_form else None,
            }
        )
