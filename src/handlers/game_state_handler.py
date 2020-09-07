from ..states.menu_state import MenuState


class GameStateHandler:
    def __init__(self, display):
        self.display = display
        self.game_states = [MenuState(display)]

    def _get_current_game_state(self):
        return self.game_states[-1]

    def tick(self, delta):
        self._get_current_game_state().tick(delta)
