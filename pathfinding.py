import pygame

import maptile
import utils

WINDOW_HEIGHT = 850
WINDOW_WIDTH = 1000

MAP_HEIGHT = 800
MAP_WIDTH = MAP_HEIGHT

ROWS = 80
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Path finding Algorithm")

bottom_info_rect = pygame.Rect(0, MAP_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT - MAP_HEIGHT)


def main(win, HEIGHT):
    grid = maptile.make_grid(ROWS, MAP_WIDTH)

    start = None
    end = None
    terrain = 'mountain'

    run = True

    while run:
        maptile.draw(win, grid, ROWS, MAP_WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: #left mouse button
                pos = pygame.mouse.get_pos()
                row, col = utils.get_clicked_pos(pos, ROWS, MAP_WIDTH)
                tile = grid[row][col]
                if not start and tile != end:
                    start = tile
                    start.make_start()
                
                elif not end and tile != start:
                    end = tile
                    end.make_end()
            
                elif tile != end and tile != start and terrain == 'mountain':
                    tile.make_barrier()

                elif tile != end and tile != start and terrain == 'water':
                    tile.make_water()

            elif pygame.mouse.get_pressed()[2]: #right mouse button
                pos = pygame.mouse.get_pos()
                row, col = utils.get_clicked_pos(pos, ROWS, MAP_WIDTH)
                tile = grid[row][col]
                tile.reset()
                if tile == start:
                    start = None
                if  tile == end:
                    end = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = maptile.make_grid(ROWS, MAP_WIDTH)

                if event.key == pygame.K_t:  
                    if terrain == 'mountain':
                        terrain = 'water'
                    else:
                        terrain = 'mountain'


    pygame.quit()

main(WIN, MAP_WIDTH)