from gapbot import Gap  # import library;

app = Gap(bot_token='your_bot_token')  # instance of Main Class;
# if you need use bot parameters you must set bot_token;


@app.on_update  # decorator for get updates; Now you can set just one handler;
def _update_handler(bot: Gap, update):  # bot: Methods;
    if update['type'] == 'text':
        bot.send_text(
            chat_id=update['chat_id'],
            text=update['data']
        )


if __name__ == '__main__':  # If you are running this module as the main program;
    app.run()  # start handler's works;
