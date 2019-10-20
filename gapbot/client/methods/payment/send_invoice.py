from gapbot.ext import BaseClient


class SendInvoice(BaseClient):
    def send_invoice(self, chat_id, amount, currency='IRR', description=None):
        return self._send(
            method='invoice',
            data={
                'chat_id': chat_id,
                'amount': amount,
                'currency': currency,
                'description': description,
            }
        )
