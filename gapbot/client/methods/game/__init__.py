from .set_game_data import SetGameData
from .get_game_data import GetGameData
from .get_top_players import GetTopPlayers


class Game(SetGameData, GetGameData, GetTopPlayers):
    pass
