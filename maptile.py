import pygame

state_color_dictionary = {
    'closed': (255, 0, 0), # Red
    'open': (0, 255, 0), # Green
    'barrier': (139,69,19), # Saddlebrown
    'start': (255, 165 ,0), #Orange
    'end': (64, 224, 208), # Turquoise
    'path': (128, 0, 128), # Purple
    'empty': (255, 255, 255), #White
    'grass': (85, 153, 0), #Strong chartreuse green
    'border': (128, 128, 128), #Grey
    'water': (28,163,236) #blue
}


class MapTile:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = state_color_dictionary['grass']
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == state_color_dictionary['closed']

    def is_open(self):
        return self.color == state_color_dictionary['open']
    
    def is_barrier(self):
        return self.color == state_color_dictionary['barrier']

    def is_water(self):
        return self.color == state_color_dictionary['water']
    
    def is_start(self):
        return self.color == state_color_dictionary['start']

    def is_end(self):
        return self.color == state_color_dictionary['end']

    def reset(self):
        self.color = state_color_dictionary['grass']

    def make_start(self):
        self.color = state_color_dictionary['start']

    def make_closed(self):
        self.color = state_color_dictionary['closed']

    def make_open(self):
        self.color = state_color_dictionary['open']
    
    def make_barrier(self):
        self.color = state_color_dictionary['barrier']

    def make_water(self):
        self.color = state_color_dictionary['water']
    
    def make_end(self):
        self.color = state_color_dictionary['end']

    def make_path(self):
        self.color = state_color_dictionary['path']

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            tile = MapTile(i,j,gap,rows)
            grid[i].append(tile)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, state_color_dictionary['border'], (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, state_color_dictionary['border'], (j * gap, 0), (j * gap , width))


def draw(win, grid, rows, width):
    win.fill(state_color_dictionary['grass'])

    for row in grid:
        for tile in row:
            tile.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()