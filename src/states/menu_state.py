import pygame
from dotmap import DotMap
from pygame.locals import MOUSEBUTTONDOWN, QUIT
from src.models.colors import WHITE
from src.utils.text import create_text, FONT_COLORS, FONT_SIZES
from .game_state import GameState
from ..configuration.configuration import DISPLAY_HEIGHT, DISPLAY_WIDTH

MENU_NAMES = DotMap(main="main", pause="pause")

ALL_MENU_OPTIONS = DotMap(start="Start", resume="Resume", main_menu="Main Menu", quit="Quit")

MENU_OPTIONS = DotMap({
    MENU_NAMES.main: [ALL_MENU_OPTIONS.start, ALL_MENU_OPTIONS.main_menu, ALL_MENU_OPTIONS.quit],
    MENU_NAMES.pause: [ALL_MENU_OPTIONS.resume, ALL_MENU_OPTIONS.main_menu, ALL_MENU_OPTIONS.quit]
})

USABLE_SCREEN_HEIGHT_MODIFIER = 0.8
USABLE_SCREEN_HEIGHT = DISPLAY_HEIGHT * USABLE_SCREEN_HEIGHT_MODIFIER
UNUSED_SCREEN_HEIGHT_MODIFIER = 1 - USABLE_SCREEN_HEIGHT_MODIFIER
MENU_Y_OFFSET = DISPLAY_HEIGHT * UNUSED_SCREEN_HEIGHT_MODIFIER / 2


class MenuState(GameState):
    def __init__(self,  display, name, on_quit, on_return_to_main_menu, on_start, background_color=WHITE):
        if name not in MENU_NAMES:
            raise ValueError(f'Attempted to push menu {name} which is invalid')

        self.background_color = background_color
        self.display = display
        self.just_clicked = False
        self.name = name
        self.on_quit = on_quit
        self.on_return_to_main_menu = on_return_to_main_menu
        self.on_start = on_start
        self.options = self._build_menu(name)

    def _build_menu(self, name):
        options = []

        x = DISPLAY_WIDTH / 2
        y = MENU_Y_OFFSET

        for menu_option in MENU_OPTIONS[name]:
            options.append(DotMap(
                name=menu_option,
                center=(x, y),
                selected=False
            ))

            y += USABLE_SCREEN_HEIGHT / len(MENU_OPTIONS[name])

        return options

    def _paint(self):
        self.display.fill(self.background_color)

        for option in self.options:
            option_text = create_text(
                color=FONT_COLORS.menu_selected if option.selected else FONT_COLORS.default,
                size=FONT_SIZES.large,
                text=option.name
            )

            option.rect = option_text.get_rect()
            option.rect.center = option.center
            self.display.blit(option_text, option.rect)

        pygame.display.update()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.on_quit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.just_clicked = True

    def _handle_selection(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for option in self.options:
            selected = pygame.Rect(option.rect).collidepoint((mouse_x, mouse_y))
            option.selected = selected

            if selected and self.just_clicked:
                self._choose_option(option.name)

    def _choose_option(self, option):
        if option not in MENU_OPTIONS[self.name]:
            raise ValueError(f'Attempted to select option {option} which is invalid for {self.name} menu')

        if option == ALL_MENU_OPTIONS.start:
            self.on_start()
        elif option == ALL_MENU_OPTIONS.main_menu:
            self.on_return_to_main_menu()
        elif option == ALL_MENU_OPTIONS.quit:
            self.on_quit()

    def tick(self, delta):
        self.just_clicked = False
        self._paint()
        self._handle_events()
        self._handle_selection()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
