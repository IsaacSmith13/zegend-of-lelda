import pygame
from src.utils.get_file_path import get_file_path_from_name, FILE_TYPES
from src.models.objects import GLOBAL_OBJECT_SIZE
from src.models.entities import DIRECTIONS, ENTITIES, MILLISECONDS_PER_FRAME


class SpriteSheet():
    def __init__(self, name, frames_per_animation, height=GLOBAL_OBJECT_SIZE, width=GLOBAL_OBJECT_SIZE):
        if name not in ENTITIES.values():
            raise ValueError(f'Attempted to load spritesheet for {name} which is invalid')

        self.frame = 0
        self.frames_per_animation = frames_per_animation
        self.height = height
        self.milliseconds_since_last_frame = 0
        self.width = width

        self.sprite_sheet = pygame.image.load(get_file_path_from_name(name, FILE_TYPES.spritesheet)).convert_alpha()
        self.current_frame = self.sprite_sheet.subsurface(0, 0, self.width, self.height)

    def get_frame(self):
        return self.current_frame

    def update_frame(self, delta, direction):
        if direction not in DIRECTIONS.values():
            raise ValueError(f'Attempted to load sprite for {direction} which is invalid')

        milliseconds_since_last_frame = delta + self.milliseconds_since_last_frame
        self.milliseconds_since_last_frame = milliseconds_since_last_frame % MILLISECONDS_PER_FRAME

        if milliseconds_since_last_frame > MILLISECONDS_PER_FRAME:
            self.frame = (self.frame + 1) % self.frames_per_animation

        base_frame_for_direction = self.frames_per_animation * direction.value
        frame_number = base_frame_for_direction + self.frame

        self.current_frame = self.sprite_sheet.subsurface(
            frame_number * self.width,
            0,
            self.width,
            self.height
        )
