class Settings():
    ''' Przechowywanie ustawien gry '''

    def __init__(self):
        ''' początkowe ustawienia gry '''
        self.screen_width = 600
        self.screen_height = 600
        self.screen_background_color = (0, 0, 0)

        self.rectangle_field_heihht = 180
        self.rectangle_field_width = 180
        self.circle_turn = True
        self.used_rectangles_list = []
        self.rectangles_dict = {}
        self.circles_fields_list =[]
        self.crosses_fields_list =[]
        self.winning_numbers_lists = [[0,1,2],[3,4,5],[6,7,8],
                                      [0,3,6],[1,4,7],[2,5,8],
                                      [0,4,8],[2,4,6]]