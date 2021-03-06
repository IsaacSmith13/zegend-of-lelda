import sys
import pygame
from ..states.menu_state import MenuState, MENU_NAMES
from ..states.level_state import LevelState, LEVEL_NAMES


class GameStateHandler:
    def __init__(self, display):
        self.display = display
        self.game_states = self._get_clean_game_state()

    def _get_clean_game_state(self):
        return [MenuState(
            display=self.display,
            name=MENU_NAMES.main,
            on_quit=self.quit_game,
            on_resume=self.unpause,
            on_return_to_main_menu=self.return_to_main_menu,
            on_start=self.start_game
        )]

    def _get_current_game_state(self):
        return self.game_states[-1]

    def tick(self, delta):
        self._get_current_game_state().tick(delta)
        pygame.display.update()

    def get_game_states(self):
        return self.game_states

    def pause(self):
        self.game_states.append(MenuState(
            display=self.display,
            name=MENU_NAMES.pause,
            on_quit=self.quit_game,
            on_resume=self.unpause,
            on_return_to_main_menu=self.return_to_main_menu,
            on_start=self.start_game
        ))

    def unpause(self):
        if self._get_current_game_state().get_name() == MENU_NAMES.pause:
            self.game_states.pop()

    def return_to_main_menu(self):
        self.game_states = self._get_clean_game_state()

    def start_game(self):
        self.game_states.append(LevelState(
            display=self.display,
            name=LEVEL_NAMES.vakariko_killage,
            on_pause=self.pause,
            on_quit=self.quit_game
        ))

    def quit_game(self):
        pygame.quit()
        sys.exit()
