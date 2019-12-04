import pygame

from pygame.sprite import Sprite

class Cross(Sprite):
    ''' Utworzenie klasy dla krzyzyka '''
    def __init__(self, screen):
        ''' inicjalizacja obiektu krzyzyka '''
        super(Cross,self).__init__()
        self.screen = screen

        #Wczytanie obrazu krzyzyka i pobranie jego prostokąta
        self.image = pygame.image.load('images/krzyzyk.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Okreslenie przykładowej pozycji kółka
        self.rect.left = self.screen_rect.left
        self.rect.top = self.screen_rect.top

    def blitme(self):
        ''' wyswietlanie krzyzyka w aktualnym polozeniu '''
        self.screen.blit(self.image, self.rect)