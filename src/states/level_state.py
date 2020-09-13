import pygame
from pygame.locals import K_a, K_d, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_s, K_UP, K_w, KEYDOWN, KEYUP, QUIT
from dotmap import DotMap
from src.objects.camera import Camera
from src.objects.entities.players.player import Player
from src.models.colors import WHITE
from src.models.entities import DIRECTIONS
from src.loaders.level_loader import load_level
from src.configuration.configuration import HORIZONTAL_TILES_ON_CAMERA, GLOBAL_OBJECT_SIZE, TILE_BUFFER, VERTICAL_TILES_ON_CAMERA
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
        self.map = pygame.Surface((HORIZONTAL_TILES_ON_CAMERA * GLOBAL_OBJECT_SIZE, VERTICAL_TILES_ON_CAMERA * GLOBAL_OBJECT_SIZE))

        self.camera = Camera(level_height=level.level_height, level_width=level.level_width)

        self.data = level.data
        self.tile_map = level.tile_map

        self.name = name

        self.on_pause = on_pause
        self.on_quit = on_quit

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

        starting_x_tile = max(self.camera.get_x_in_tiles(), 0)
        ending_x_tile = min(self.camera.get_x_in_tiles() + HORIZONTAL_TILES_ON_CAMERA, len(self.tile_map[0]))

        starting_y_tile = max(self.camera.get_y_in_tiles(), 0)
        ending_y_tile = min(self.camera.get_y_in_tiles() + VERTICAL_TILES_ON_CAMERA, len(self.tile_map[0][0]))

        for layer in self.tile_map:
            x_display = 0

            for x in range(starting_x_tile, ending_x_tile):
                y_display = 0

                for y in range(starting_y_tile, ending_y_tile):
                    asset = self.data.get_tile_image_by_gid(layer[x][y])

                    if asset:
                        self.map.blit(asset, (x_display, y_display))

                    y_display += GLOBAL_OBJECT_SIZE

                x_display += GLOBAL_OBJECT_SIZE

        self.display.blit(self.map, (self.camera.get_x_offset(), self.camera.get_y_offset()))
        self.display.blit(self.player.image, (self.player.get_x() - self.camera.get_x(), self.player.get_y() - self.camera.get_y()))

    def tick(self, delta):
        self._handle_events()
        self.player.tick(delta)

        self.camera.set_x(self.player.get_x())
        self.camera.set_y(self.player.get_y())

        self._paint()

    def get_name(self):
        return self.name
