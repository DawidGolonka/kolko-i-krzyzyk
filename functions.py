import sys
import pygame
import time
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

def create_menu(screen, kk_settings):
    ''' wyswietlanie tablicy z Menu gry '''
    while kk_settings.menu:
        clock = pygame.time.Clock()
        new_game_button = pygame.image.load('images/newgame.bmp')
        new_game_button_rect = new_game_button.get_rect()
        new_game_button_rect.centerx = 150
        new_game_button_rect.centery = 150
        end_game_button = pygame.image.load('images/end.bmp')
        end_game_button_rect = end_game_button.get_rect()
        end_game_button_rect.centerx = 150
        end_game_button_rect.centery = 300
        screen.blit(new_game_button, (new_game_button_rect.centerx, new_game_button_rect.centery))
        screen.blit(end_game_button, (end_game_button_rect.centerx, end_game_button_rect.centery))
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x >= new_game_button_rect.left and mouse_x <= new_game_button_rect.right and \
                        mouse_y >= new_game_button_rect.top and mouse_y <= new_game_button_rect.bottom:
                    kk_settings.game_running = True
                    kk_settings.menu = False
                elif mouse_x >= end_game_button_rect.left and mouse_x <= end_game_button_rect.right and \
                        mouse_y >= end_game_button_rect.top and mouse_y <= end_game_button_rect.bottom:
                    kk_settings.game_running = False
                    kk_settings.menu = False
                else:
                    continue


def finish_game(screen, color, kk_settings, width, circles, crosses):
    ''' Rysowanie linii zwyciestwa '''
    pygame.draw.line(screen, color, (kk_settings.line_beg_x, kk_settings.line_beg_y), (kk_settings.line_end_x, kk_settings.line_end_y), width)
    pygame.display.flip()
    time.sleep(2)
    kk_settings.used_rectangles_list.clear()
    circles.empty()
    crosses.empty()
    kk_settings.circles_fields_list.clear()
    kk_settings.crosses_fields_list.clear()
    kk_settings.menu = True
    create_menu(screen, kk_settings)


def update_screen(kk_settings, screen, rectangles, circles, crosses):
    ''' Odswiezanie ekranu  '''
    # odwiezenie ekranu po przejsciu kazdej iteracji
    screen.fill(kk_settings.screen_background_color)
    #wyswietlenie prostokatow planszy
    rectangles.draw(screen)
    circles.draw(screen)
    crosses.draw(screen)
    #pygame.draw.line(screen, (10, 10, 11), (kk_settings.line_beg_x, kk_settings.line_beg_y), (kk_settings.line_end_x, kk_settings.line_end_y), 20)
    #Wyswietlanie ostatniej wersji ekranu
    pygame.display.update()
    if kk_settings.menu:
        finish_game(screen, (10, 11, 10), kk_settings, 20, circles, crosses)
    if (len(kk_settings.used_rectangles_list)) == 9:
        finish_game(screen, (10, 11, 10), kk_settings, 0, circles, crosses)


def create_rectangles(kk_settings, screen, rectangles):
    ''' fukcja ma utworzyć prostokąty ktore stanowią plansze '''
    i = 0
    for positionx in range(100, 501, 200):
        for positiony in range(100, 501, 200):
            rectangle = Rectangle(screen, kk_settings, 'images/prostokat.bmp')
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
    print(currently_fields_list)
    ''' 
       if currently_fields_list in kk_settings.winning_numbers_list:
            kk_settings.line_beg_x = (kk_settings.rectangles_dict[currently_fields_list[0]].centerx)
            kk_settings.line_beg_y = (kk_settings.rectangles_dict[currently_fields_list[0]].centery)
            kk_settings.line_end_x = (kk_settings.rectangles_dict[currently_fields_list[2]].centerx)
            kk_settings.line_end_y = (kk_settings.rectangles_dict[currently_fields_list[2]].centery)
            kk_settings.menu = True
        '''
    if len(currently_fields_list) > 2:
        currently_fields_set = set()
        for currently_field in currently_fields_list:
            currently_fields_set.add(currently_field)

        for i in range(0,8):
            winning_numbers_set_basic = set()
            for winning_number in kk_settings.winning_numbers_list_basic[i]:
                winning_numbers_set_basic.add(winning_number)
            if winning_numbers_set_basic.issubset(currently_fields_set):
                print(winning_numbers_set_basic)
                print(currently_fields_set)
                kk_settings.line_beg_x = (kk_settings.rectangles_dict[kk_settings.winning_numbers_list_basic[i][0]].centerx)
                kk_settings.line_beg_y = (kk_settings.rectangles_dict[kk_settings.winning_numbers_list_basic[i][0]].centery)
                kk_settings.line_end_x = (kk_settings.rectangles_dict[kk_settings.winning_numbers_list_basic[i][2]].centerx)
                kk_settings.line_end_y = (kk_settings.rectangles_dict[kk_settings.winning_numbers_list_basic[i][2]].centery)
                kk_settings.menu = True


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