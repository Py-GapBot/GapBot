from .send_text import SendText
from .send_image import SendImage
from .send_audio import SendAudio
from .send_video import SendVideo


class Messages(SendText, SendImage, SendAudio, SendVideo):
    pass
