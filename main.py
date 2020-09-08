import pygame
from src.configuration.configuration import DISPLAY_HEIGHT, DISPLAY_WIDTH, FPS, GAME_NAME
from src.handlers.game_state_handler import GameStateHandler


def main():
    pygame.init()

    pygame.display.set_caption(GAME_NAME)

    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    game_state_handler = GameStateHandler(display)

    clock = pygame.time.Clock()

    while True:
        delta = clock.tick(FPS)
        game_state_handler.tick(delta)


main()
