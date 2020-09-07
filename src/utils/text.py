from dotmap import DotMap
import pygame
from src.models.colors import BLACK, PINK

FONT = 'freesansbold.ttf'
FONT_COLORS = DotMap(default=BLACK, menu_selected=PINK)
FONT_SIZES = DotMap(small=16, medium=32, large=64)


def create_text(size, text, color=FONT_COLORS.default):
    if size not in FONT_SIZES.values():
        raise ValueError(f'Attempted to use font size {size} which is invalid')

    if color not in FONT_COLORS.values():
        raise ValueError(f'Attempted to use font color {color} which is invalid')

    return pygame.font.Font(FONT, size).render(text, True, color)
