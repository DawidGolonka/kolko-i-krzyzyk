import sys

import pygame
import settings
import functions
from pygame.sprite import Group

def run_game():
    ''' Inicjalizacja gry i utworzenie ekranu '''
    pygame.init()
    kk_settings = settings.Settings()
    screen = pygame.display.set_mode((kk_settings.screen_width, kk_settings.screen_height))
    pygame.display.set_caption('Kołko i krzyżyk')
    rectangles = Group()
    circles = Group()
    crosses = Group()

    #utworzenie prostokatów planszy
    functions.create_rectangles(kk_settings, screen, rectangles)

    #rozpoczęcie pętli głównej gry
    while True:
        #sprawdzanie myszki i klawiatury
        functions.check_events(rectangles, screen, circles, kk_settings, crosses)

        #odwiezenie ekranu po przejsciu kazdej iteracji
        functions.update_screen(kk_settings, screen, rectangles, circles, crosses)
run_game()

