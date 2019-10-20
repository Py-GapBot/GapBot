from .send_text import SendText
from .send_image import SendImage
from .send_audio import SendAudio
from .send_video import SendVideo
from .send_voice import SendVoice
from .send_file import SendFile
from .send_contact import SendContact
from .send_action import SendAction
from .edit_message import EditMessage
from .delete_message import DeleteMessage


class Messages(
    SendText,
    SendImage,
    SendAudio,
    SendVideo,
    SendVoice,
    SendFile,
    SendContact,
    SendAction,
    EditMessage,
    DeleteMessage
):
    pass
