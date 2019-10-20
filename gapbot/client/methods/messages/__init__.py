from .send_text import SendText
from .send_image import SendImage
from .send_audio import SendAudio


class Messages(SendText, SendImage, SendAudio):
    pass
