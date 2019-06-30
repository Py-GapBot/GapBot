from gapbot.ext import BaseClient
from json import dumps


class SendImage(BaseClient):
    def send_image(self, chat_id, path):
        return self._send(
            method='sendMessage',
            data={
                'chat_id': chat_id,
                'type': 'image',
                'data': dumps(self.upload(chat_id=chat_id, file_type='image', path=path).json()),
            }
        )
