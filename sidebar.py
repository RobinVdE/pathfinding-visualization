
import pygame

class SideBar():
    def __init__(self, win_height, win_width, map_width):
        #Dimensions of the sidescreen and its location to be blitted from
        self.side_w = win_width
        self.side_h = win_height
        self.side_x = map_width
        self.side_y = 0
        #color of sidebar
        self.color = (211,211,211)
        #button size
        self.b_size = 65
        
    def draw_sidebar(self, win):
        #draw sidescreen
        pygame.draw.rect(win, self.color, (self.side_x, self.side_y, self.side_w, self.side_h))

def make_sidebar(win_height, win_width, map_width):
    sidebar = SideBar(win_height, win_width, map_width)
    return sidebar



        
