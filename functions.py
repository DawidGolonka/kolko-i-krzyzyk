import sys
import pygame
from classes import Rectangle
from classes import CircleCross


def check_events(rectangles, screen, circles, kk_settings, crosses):
    ''' funckja sprawdzająca iterakcje użytkownika '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_rectangle_clicked(mouse_x, mouse_y, rectangles, screen, circles, kk_settings, crosses)


def update_screen(kk_settings, screen, rectangles, circles, crosses):
    ''' Odswiezanie ekranu  '''
    # odwiezenie ekranu po przejsciu kazdej iteracji
    screen.fill(kk_settings.screen_background_color)
    #wyswietlenie prostokatow planszy
    rectangles.draw(screen)
    circles.draw(screen)
    crosses.draw(screen)
    pygame.draw.line(screen, (10, 10, 11), (kk_settings.line_beg_x, kk_settings.line_beg_y), (kk_settings.line_end_x, kk_settings.line_end_y), 20)
    #Wyswietlanie ostatniej wersji ekranu
    pygame.display.flip()

def create_rectangles(kk_settings, screen, rectangles):
    ''' fukcja ma utworzyć prostokąty ktore stanowią plansze '''
    i = 0
    for positionx in range(100, 501, 200):
        for positiony in range(100, 501, 200):
            rectangle = Rectangle(screen, kk_settings)
            rectangle.rect.centerx = positionx
            rectangle.rect.centery = positiony
            rectangles.add(rectangle)
            #robienie słownika numer prostokata:polozenie
            kk_settings.rectangles_dict[i] = rectangle.rect
            i += 1

def create_circles(screen, position_figurex, position_figurey, circles):
    ''' fukcja ma utworzyć prostokąty ktore stanowią plansze '''
    circle_bmp = 'images/kolko.bmp'
    circle = CircleCross(screen, circle_bmp)
    circle.rect.centerx =  position_figurex
    circle.rect.centery = position_figurey
    circles.add(circle)

def create_crosses(screen, position_figurex, position_figurey, crosses):
    ''' fukcja ma utworzyć prostokąty ktore stanowią plansze '''
    cross_bmp = 'images/krzyzyk.bmp'
    cross = CircleCross(screen, cross_bmp)
    cross.rect.centerx =  position_figurex
    cross.rect.centery = position_figurey
    crosses.add(cross)

def winning_check(currently_fields_list, kk_settings):
    ''' funkcja sprawdzajaca czy osoby juz wygrala'''
    if currently_fields_list in kk_settings.winning_numbers_lists:
        kk_settings.line_beg_x = (kk_settings.rectangles_dict[currently_fields_list[0]].centerx)
        kk_settings.line_beg_y = (kk_settings.rectangles_dict[currently_fields_list[0]].centery)
        kk_settings.line_end_x = (kk_settings.rectangles_dict[currently_fields_list[2]].centerx)
        kk_settings.line_end_y = (kk_settings.rectangles_dict[currently_fields_list[2]].centery)


        print(currently_fields_list)
        print(kk_settings.winning_numbers_lists)
        print(kk_settings.winning_numbers_lists.index(currently_fields_list))



def check_rectangle_clicked(mouse_x, mouse_y, rectangles, screen, circles, kk_settings, crosses):
    ''' oblusga klikniecia prostokąta myszka'''
    for rectangle in rectangles:
        if mouse_x >= rectangle.rect.left and mouse_x <= rectangle.rect.right and \
        mouse_y >= rectangle.rect.top and mouse_y <= rectangle.rect.bottom and \
                rectangle.rect not in kk_settings.used_rectangles_list:
            position_figurex = rectangle.rect.centerx
            position_figurey = rectangle.rect.centery
            kk_settings.used_rectangles_list.append(rectangle.rect)
            if kk_settings.circle_turn:
                create_circles(screen, position_figurex, position_figurey, circles)
                kk_settings.circle_turn = False
                for rectangle_number, rectangle_rect in kk_settings.rectangles_dict.items():
                    if rectangle.rect == rectangle_rect:
                        kk_settings.circles_fields_list.append(rectangle_number)
                        kk_settings.circles_fields_list.sort()
                        winning_check(kk_settings.circles_fields_list, kk_settings)
            elif not kk_settings.circle_turn:
                create_crosses(screen, position_figurex, position_figurey, crosses)
                kk_settings.circle_turn = True
                for rectangle_number, rectangle_rect in kk_settings.rectangles_dict.items():
                    if rectangle.rect == rectangle_rect:
                        kk_settings.crosses_fields_list.append(rectangle_number)
                        kk_settings.crosses_fields_list.sort()
                        winning_check(kk_settings.crosses_fields_list, kk_settings)