import pygame

class Line():
    ''' Tworzenie lini wygrania '''
    def __init__(self, screen, line_beg_x, line_beg_y, line_end_x, line_end_y):
        ''' inicjalizacja '''
        self.screen = screen
        self.line = pygame.Line(screen, (200, 200, 200), (line_beg_x, line_beg_y), (line_end_x, line_end_y), 100)

    def print_line(self):
        pygame.draw.line(self.line)