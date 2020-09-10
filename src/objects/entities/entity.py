import pygame
from src.objects.entities.sprite_sheet import SpriteSheet, ENTITIES
from src.models.objects import GLOBAL_OBJECT_SIZE
from src.models.entities import DIRECTIONS


class Entity(pygame.sprite.Sprite):
    def __init__(
            self,
            frames_per_animation,
            name,
            movespeed,
            x,
            y,
            height=GLOBAL_OBJECT_SIZE,
            width=GLOBAL_OBJECT_SIZE
    ):
        super().__init__()

        self.current_directions = []
        self.height = height
        self.movespeed = movespeed
        self.width = width
        self.x = x
        self.y = y

        self.sprite_sheet = SpriteSheet(
            ENTITIES[name],
            frames_per_animation=frames_per_animation,
            height=height,
            width=width
        )

        self.image = self.sprite_sheet.get_frame()
        self.rect = pygame.Rect(x, y, width, height)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_movespeed(self):
        return self.movespeed

    def set_movespeed(self, movespeed):
        self.movespeed = movespeed

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x
        self.rect = pygame.Rect(x, self.y, self.width, self.height)

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y
        self.rect = pygame.Rect(self.x, y, self.width, self.height)

    def add_direction(self, direction):
        if direction not in self.current_directions:
            self.current_directions.append(direction)

    def remove_direction(self, direction):
        if direction in self.current_directions:
            self.current_directions.remove(direction)

    def tick(self, delta):
        if len(self.current_directions) == 0:
            return

        right = down = left = up = False

        for direction in self.current_directions:
            if direction == DIRECTIONS.right and not left:
                right = True
                self.set_x(self.x + self.movespeed * delta)
            elif direction == DIRECTIONS.down and not up:
                down = True
                self.set_y(self.y + self.movespeed * delta)
            elif direction == DIRECTIONS.left and not right:
                left = True
                self.set_x(self.x - self.movespeed * delta)
            elif direction == DIRECTIONS.up and not down:
                up = True
                self.set_y(self.y - self.movespeed * delta)

        self.sprite_sheet.update_frame(delta=delta, direction=self.current_directions[0])
        self.image = self.sprite_sheet.get_frame()
