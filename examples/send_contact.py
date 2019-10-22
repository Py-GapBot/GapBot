from gapbot import Gap  # import library;
from platform import system

app = Gap(bot_token='your_bot_token')  # instance of Main Class;
# if you need use bot parameters you must set bot_token;

if __name__ == '__main__':  # If you are running this module as the main program;
    target_id = 000000  # whose to be send text to him;
    app.send_contact(
        chat_id=target_id,
        name='Gap',
        phone='+989123456789',
        caption='Gap Caption'
    )

# https://developer.gap.im/doc/botplatform#method-send-contact
