from gapbot.ext import BaseClient


class GetInvoiceStatus(BaseClient):
    def get_invoice_status(self, chat_id, invoice_id):
        return self._send(
            method='invoice/inquiry',
            data={
                'chat_id': chat_id,
                'ref_id': invoice_id,
            }
        )
