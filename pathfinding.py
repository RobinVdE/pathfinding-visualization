import pygame
import pygame_gui

import maptile
import utils

HEIGHT = 800
WIDTH = 1000
ROWS = 80
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

pygame.display.set_caption("Path finding Algorithm")

def main(win, HEIGHT):
    grid = maptile.make_grid(ROWS, HEIGHT)

    start = None
    end = None
    terrain = 'mountain'

    run = True

    while run:
        maptile.draw(win, grid, ROWS, HEIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: #left mouse button
                pos = pygame.mouse.get_pos()
                row, col = utils.get_clicked_pos(pos, ROWS, HEIGHT)
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
                row, col = utils.get_clicked_pos(pos, ROWS, HEIGHT)
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
                    grid = maptile.make_grid(ROWS, HEIGHT)

                if event.key == pygame.K_t:
                    terrain = 'water'

    pygame.quit()

main(WIN, HEIGHT)