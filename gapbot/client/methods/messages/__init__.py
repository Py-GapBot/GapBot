from .send_text import SendText
from .send_image import SendImage


class Messages(SendText, SendImage):
    pass
