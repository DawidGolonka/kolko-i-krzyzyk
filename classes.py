import pygame
import copy
from pygame.sprite import Sprite

class CircleCross(Sprite):
    ''' Utworzenie klasy dla krzyzyka i kolka '''

    def __init__(self, screen, source_bmp):
        ''' inicjalizacja obiektu krzyzyka '''
        super().__init__()
        self.screen = screen
        self.source_bmp = source_bmp

        #Wczytanie obrazu krzyzyka i pobranie jego prostokąta
        self.image = pygame.image.load(self.source_bmp)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Okreslenie przykładowej pozycji kółka
        self.rect.left = self.screen_rect.left
        self.rect.top = self.screen_rect.top


class Settings():
    ''' Przechowywanie ustawien gry '''

    def __init__(self):
        ''' początkowe ustawienia gry '''
        self.screen_width = 600
        self.screen_height = 600
        self.new_game_button_centerx = 300
        self.new_game_button_centery = 150
        self.end_game_button_centerx = 300
        self.end_game_button_centery = 450
        self.screen_background_color = (0, 0, 0)

        self.rectangle_field_heihht = 180
        self.rectangle_field_width = 180
        self.menu = True
        self.circle_turn = True
        self.game_running = True
        self.used_rectangles_list = []
        self.rectangles_dict = {}
        self.circles_fields_list =[]
        self.crosses_fields_list =[]
        self.winning_numbers_list_basic = [[0,1,2],[3,4,5],[6,7,8],
                                      [0,3,6],[1,4,7],[2,5,8],
                                      [0,4,8],[2,4,6]]
        self.line_beg_x, self.line_beg_y, self.line_end_x, self.line_end_y = 0,0,0,0



class Rectangle(Sprite):
    ''' Klasa przedstawiajaca pojedynczy prostokąt tła w planszy '''

    def __init__(self, screen, kk_settings, rect_source):
        ''' inicjalizacja prostokąta i zdefiniowanie polozenia '''
        super().__init__()
        self.screen = screen
        self.kk_settings = kk_settings

        #wczytanie obrazu prostokata
        self.image = pygame.image.load(rect_source)
        self.rect = self.image.get_rect()

        self.rect.centerx = 0
        self.rect.centery = 0

