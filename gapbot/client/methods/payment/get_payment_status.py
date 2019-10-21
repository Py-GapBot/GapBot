from gapbot.ext import BaseClient


class GetPaymentStatus(BaseClient):
    def get_payment_status(self, chat_id, payment_id):
        return self._send(
            method='payment/inquiry',
            data={
                'chat_id': chat_id,
                'ref_id': payment_id,
            }
        )
