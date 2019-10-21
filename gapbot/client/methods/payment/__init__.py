from .send_invoice import SendInvoice
from .verify_invoice import VerifyInvoice


class Payment(SendInvoice, VerifyInvoice):
    pass
