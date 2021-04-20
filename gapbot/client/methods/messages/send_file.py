from gapbot.ext import BaseClient
from json import dumps


class SendFile(BaseClient):
    def send_file(self, chat_id, path, caption=None, file_name=None, reply_keyboard=None, inline_keyboard=None, reply_form=None):
        return self._send(
            method='sendMessage',
            data={
                'chat_id': chat_id,
                'type': 'file',
                'data': self.upload(chat_id=chat_id, file_type='file', path=path, file_name=file_name, desc=caption),
                'reply_keyboard': dumps(reply_keyboard) if reply_keyboard else None,
                'inline_keyboard': dumps(inline_keyboard) if inline_keyboard else None,
                'form': dumps(reply_form) if reply_form else None,
            }
        )
