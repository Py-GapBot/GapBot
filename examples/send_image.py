from gapbot import Gap  # import library;
from platform import system

app = Gap(bot_token='your_bot_token')  # instance of Main Class;
# if you need use bot parameters you must set bot_token;

if __name__ == '__main__':  # If you are running this module as the main program;
    target_id = 000000  # whose to be send text to him;
    if system().lower() == 'windows':  # Windows users
        image_path = r'C:\Users\GapUser\Gap.png'
    else:  # Gnu/linux users and others (not windows)
        image_path = r'/home/GapUser/Gap.png'
    app.send_image(
        chat_id=target_id,
        path=image_path
    )

# https://developer.gap.im/doc/botplatform#method-send-image
