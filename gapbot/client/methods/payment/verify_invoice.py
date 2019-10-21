from gapbot.ext import BaseClient


class VerifyInvoice(BaseClient):
    def verify_invoice(self, chat_id, invoice_id):
        return self._send(
            method='invoice/verify',
            data={
                'chat_id': chat_id,
                'ref_id': invoice_id,
            }
        )
