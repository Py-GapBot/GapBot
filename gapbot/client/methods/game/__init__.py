from .set_game_data import SetGameData
from .get_game_data import GetGameData
from .get_top_players import GetTopPlayers
from .get_game_config import GetGameConfig


class Game(SetGameData, GetGameData, GetTopPlayers, GetGameConfig):
    pass
