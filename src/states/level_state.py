import pygame
from dotmap import DotMap
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from src.models.colors import WHITE
from .game_state import GameState

LEVEL_NAMES = DotMap(vakariko_killage="Vakariko Killage")


class LevelState(GameState):
    def __init__(self, display, name, on_pause, on_quit):
        if name not in LEVEL_NAMES.values():
            raise ValueError(f'Attempted to push level {name} which is invalid')

        self.display = display
        self.name = name
        self.on_pause = on_pause
        self.on_quit = on_quit

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.on_quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.on_pause()

    def _paint(self):
        self.display.fill(WHITE)

    def tick(self, delta):
        self._handle_events()
        self._paint()

    def get_name(self):
        return self.name
