import pygame
from src.configuration.configuration import GLOBAL_OBJECT_SIZE


class Object(pygame.sprite.Sprite):
    def __init__(self, collidable, image, x, y, height=GLOBAL_OBJECT_SIZE, width=GLOBAL_OBJECT_SIZE):
        super().__init__()

        self.height = height
        self.width = width

        self.x = x
        self.y = y

        self.collidable = collidable
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)

    def _generate_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def is_collidable(self):
        return self.collidable

    def set_collidable(self, collidable):
        self.collidable = collidable

    def get_image(self):
        return self.image

    def get_rect(self):
        return self.rect

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x
        self._generate_rect()

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y
        self._generate_rect()
