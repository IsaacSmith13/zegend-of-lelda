from .game_state import GameState


class MenuState(GameState):
    def __init__(self,  display):
        self.display = display

    def _paint(self):
        pass

    def tick(self, delta):
        self._paint()
