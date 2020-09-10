import pygame
from pygame.locals import K_a, K_d, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_s, K_UP, K_w, KEYDOWN, KEYUP, QUIT
from dotmap import DotMap
from src.objects.entities.players.player import Player
from src.models.colors import WHITE
from src.models.entities import DIRECTIONS
from src.loaders.level_loader import load_level
from .game_state import GameState


LEVEL_NAMES = DotMap(vakariko_killage="Vakariko Killage")


class LevelState(GameState):
    def __init__(self, display, name, on_pause, on_quit):
        if name not in LEVEL_NAMES.values():
            raise ValueError(f'Attempted to push level {name} which is invalid')

        level = load_level(name)

        if not level:
            raise ValueError(f'failed to load level {name}')

        self.display = display
        self.level_height = level.level_height
        self.level_width = level.level_width
        self.name = name
        self.on_pause = on_pause
        self.on_quit = on_quit
        self.tile_height = level.tile_height
        self.tile_map = level.tile_map
        self.tile_width = level.tile_width

        self.player = Player()
        self.player_group = pygame.sprite.Group(self.player)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.on_quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.on_pause()
                elif event.key == K_d or event.key == K_RIGHT:
                    self.player.add_direction(DIRECTIONS.right)
                elif event.key == K_s or event.key == K_DOWN:
                    self.player.add_direction(DIRECTIONS.down)
                elif event.key == K_a or event.key == K_LEFT:
                    self.player.add_direction(DIRECTIONS.left)
                elif event.key == K_w or event.key == K_UP:
                    self.player.add_direction(DIRECTIONS.up)
            elif event.type == KEYUP:
                if event.key == K_d or event.key == K_RIGHT:
                    self.player.remove_direction(DIRECTIONS.right)
                elif event.key == K_s or event.key == K_DOWN:
                    self.player.remove_direction(DIRECTIONS.down)
                elif event.key == K_a or event.key == K_LEFT:
                    self.player.remove_direction(DIRECTIONS.left)
                elif event.key == K_w or event.key == K_UP:
                    self.player.remove_direction(DIRECTIONS.up)

    def _paint(self):
        self.display.fill(WHITE)

        for layer in self.tile_map:
            for tile in layer:
                if tile:
                    self.display.blit(tile.asset, (tile.x, tile.y))

        self.player_group.draw(self.display)

    def tick(self, delta):
        self._handle_events()
        self.player.tick(delta)
        self._paint()

    def get_name(self):
        return self.name
