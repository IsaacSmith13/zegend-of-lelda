from .game_state import GameState


class LevelState(GameState):
    def __init__(self, name):
        self.name = name

    def _paint(self):
        pass

    def tick(self, delta):
        self._paint()
