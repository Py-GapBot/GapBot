from gapbot import Gap

app = Gap(
    bot_token='6327819b0a5a3401bd11f616b9f5d2754e24162610b2a39f94fd299485ff3175'
)


@app.on_update
def _update_handler(bot: Gap, update):
    print('{}'.format(update))


if __name__ == '__main__':
    app.run()
