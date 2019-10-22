from gapbot.ext import BaseClient
from json import dumps as json_dumps


class Upload(BaseClient):
    def upload(self, chat_id, file_type, path, desc=None):
        file_types = ('image', 'video', 'voice', 'audio', 'file')
        if file_type not in file_types:
            return
        with open(path, 'rb') as file:
            send_result = self._send(
                method='upload',
                data={'chat_id': chat_id, 'desc': desc},
                files={file_type: file.read()}
            ).json()
            send_result['desc'] = desc
            return json_dumps(send_result)
