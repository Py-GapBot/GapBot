from .send_invoice import SendInvoice
from .verify_invoice import VerifyInvoice
from .get_invoice_status import GetInvoiceStatus
from .verify_payment import VerifyPayment
from .get_payment_status import GetPaymentStatus


class Payment(SendInvoice, VerifyInvoice, GetInvoiceStatus, VerifyPayment, GetPaymentStatus):
    pass
