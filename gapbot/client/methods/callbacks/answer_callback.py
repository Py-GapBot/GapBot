from gapbot.ext import BaseClient


class AnswerCallback(BaseClient):
    def answer_callback(self, chat_id, callback_id, text, alert=True):
        return self._send(
            method='answerCallback',
            data={
                'chat_id': chat_id,
                'callback_id': callback_id,
                'text': text,
                'alert': alert,
            }
        )
