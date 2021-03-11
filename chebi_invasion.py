import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien

import game_functions as gf


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Chebi Invasion")
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    # Создание пришельца.
    alien = Alien(ai_settings, screen)
    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # Удаление пуль, вышедших за край экрана.
        gf.update_screen(ai_settings, screen, ship, bullets, alien)
run_game()
