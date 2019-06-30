from gapbot import Gap  # import library;

app = Gap()  # instance of Main Class;
# if you just need get update you don't must set bot_token;


@app.on_update  # decorator for get updates; Now you can set just one handler;
def _update_handler(bot: Gap, update):  # bot: Methods;
    print('{}'.format(update))  # Cast Update as dict to string then print it;


if __name__ == '__main__':  # If you are running this module as the main program;
    app.run()  # start handler's works;
