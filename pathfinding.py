import pygame
import maptile
import utils

WIDTH = 800
ROWS = 80
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path finding Algorithm")

def main(win, width):
    grid = maptile.make_grid(ROWS, width)

    start = None
    end = None

    run = True

    while run:
        maptile.draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: #left mouse button
                pos = pygame.mouse.get_pos()
                row, col = utils.get_clicked_pos(pos, ROWS, width)
                tile = grid[row][col]
                if not start and tile != end:
                    start = tile
                    start.make_start()
                
                elif not end and tile != start:
                    end = tile
                    end.make_end()
            
                elif tile != end and tile != start:
                    tile.make_barrier()

            elif pygame.mouse.get_pressed()[2]: #right mouse button
                pos = pygame.mouse.get_pos()
                row, col = utils.get_clicked_pos(pos, ROWS, width)
                tile = grid[row][col]
                tile.reset()
                if tile == start:
                    start = None
                if  tile == end:
                    end = None
            

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = maptile.make_grid(ROWS, width)

    pygame.quit()

main(WIN, WIDTH)