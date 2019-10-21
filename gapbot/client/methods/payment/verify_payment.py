from gapbot.ext import BaseClient


class VerifyPayment(BaseClient):
    def verify_payment(self, chat_id, payment_id):
        return self._send(
            method='payment/verify',
            data={
                'chat_id': chat_id,
                'ref_id': payment_id,
            }
        )
