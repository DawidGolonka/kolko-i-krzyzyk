import pygame

from pygame.sprite import Sprite
class Circle(Sprite):
    ''' Utworzenie klasy dla kółka '''

    def __init__(self, screen):
        ''' inicjalizacja obiektu kółka '''
        super(Circle, self).__init__()
        self.screen = screen

        #Wczytanie obrazu kółka i pobranie jego prostokąta
        self.image = pygame.image.load('images/kolko.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Okreslenie przykładowej pozycji kółka
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        ''' wyswietlanie kolka w aktualnym polozeniu '''
        self.screen.blit(self.image, self.rect)