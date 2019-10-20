from gapbot.ext import BaseClient
from json import dumps


class SendContact(BaseClient):
    def send_contact(self, chat_id, name, phone, reply_keyboard=None, inline_keyboard=None, reply_form=None):
        return self._send(
            method='sendMessage',
            data={
                'chat_id': chat_id,
                'type': 'contact',
                'data': dumps({'name': name, 'phone': phone}),
                'reply_keyboard': dumps(reply_keyboard) if reply_keyboard else None,
                'inline_keyboard': dumps(inline_keyboard) if inline_keyboard else None,
                'form': dumps(reply_form) if reply_form else None,
            }
        )
