from GapBot.ext import BaseClient


class OnUpdate(BaseClient):
    def on_update(self, func):
        def inner(text, count):
            func(text, count)
        self.handler = inner
        return inner
