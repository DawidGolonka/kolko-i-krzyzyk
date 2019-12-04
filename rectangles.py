import pygame

from pygame.sprite import Sprite

class Rectangle(Sprite):
    ''' Klasa przedstawiajaca pojedynczy prostokąt tła w planszy '''
    def __init__(self, screen, kk_settings):
        ''' inicjalizacja prostokąta i zdefiniowanie polozenia '''
        super(Rectangle, self).__init__()
        self.screen = screen
        self.kk_settings = kk_settings

        #wczytanie obrazu prostokata
        self.image = pygame.image.load('images/prostokat.bmp')
        self.rect = self.image.get_rect()

        self.rect.centerx = 0
        self.rect.centery = 0

    def blitme(self):
        ''' Wyswietlanie prostokata w jego polozeniu'''
        self.screen.blit(self.image, self.rect)
