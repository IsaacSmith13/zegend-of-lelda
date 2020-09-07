import os
import pygame
from configuration import DISPLAY_HEIGHT, DISPLAY_WIDTH, FPS, GAME_NAME

ROOT_PATH = os.path.dirname(__file__)


def main():
    pygame.init()

    pygame.display.set_caption(GAME_NAME)

    pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

main()
