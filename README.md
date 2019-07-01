<p align="center">
    <a href="https://github.com/MrMahdi313/GapBot">
        <img src="https://gap.im/img/gap-splash.png" alt="GapBot">
    </a>
    <br>
    <b>Gap Messenger Api Bot Library for Python</b>
    <br>
    <a href="https://gapbot.readthedocs.io/en/latest/">
        Documentation(coming soon)
    </a>
    •
    <a href="https://github.com/MrMahdi313/GapBot/releases">
        Releases
    </a>
</p>


## GapBot

``` python
from gapbot import Gap

app = Gap()


@app.on_update
def _update_handler(bot, update):
    prin('{}'.format(update))


if __name__ == '__main__':
    app.run()
```

**GapBot** is an elegant, easy-to-use [Gap](https://gap.im/) Bot library written from the
ground up in Python. It enables you to easily create custom apps.

> [GapBot in fully-asynchronous mode is commin soon »](https://github.com/MrMahdi313/GapBot/tree/async)
>
> [GapBot in plugin base mode is commin soon »](https://github.com/MrMahdi313/GapBot)

### Features

- **Easy**: You can install GapBot with pip and start building your applications right away.
- **Elegant**: Low-level details are abstracted and re-presented in a much nicer and easier way.

### Requirements

- Python 3.6 or higher.
- A [Gap Bot Token](https://developer.gap.im/signin).

### Installing

``` bash
pip3 install GapBot
```

### Resources

- The Docs contain lots of resources to help you getting started with GapBot:
 https://gapbot.readthedocs.io/en/latest (coming soon).
- Reading [Examples in this repository](https://github.com/MrMahdi313/GapBot/tree/master/examples) is also a good way
  for learning how GapBot works.
- For other requests you can send an [Email](mailto:m.m.z.m12363@gmail.com) or a [Message](https://t.me/Mr_Mahdi313).

### Contributing

GapBot is brand new, and **you are welcome to try it and help make it even better** by either submitting pull
requests or reporting issues/bugs as well as suggesting best practices, ideas, enhancements on both code
and documentation. Any help is appreciated!

### Copyright & License

- Copyright (C) 2017-2019 MohammadMahdi Zojaji as <<https://github.com/MrMahdi313>>
- Licensed under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+)
