from .send_invoice import SendInvoice
from .verify_invoice import VerifyInvoice
from .get_invoice_status import GetInvoiceStatus


class Payment(SendInvoice, VerifyInvoice, GetInvoiceStatus):
    pass
