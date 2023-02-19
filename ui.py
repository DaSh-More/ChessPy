import pygame as pg
from desk import Desk
import numpy as np
from loguru import logger
logger.enable('chess_figures')


img_path = "./src/img/"
pg.init()
screen = pg.display.set_mode((1200, 700))

cell_size = 80


class VisualDesk(Desk, pg.Surface):
    def __init__(self):
        Desk.__init__(self, size=cell_size)
        pg.Surface.__init__(self, (cell_size*8, cell_size*8))

        self.display_figures()

    def draw_cells(self):
        colors = ('#759455', '#eceed2')
        for row in range(8):
            for col in range(8):
                pg.draw.rect(self, colors[(row+col) % 2],
                             (row*cell_size, col*cell_size,
                              cell_size, cell_size))

    def __draw_figure(self, figure):

        self.blit(figure.image, figure.rect)
        logger.debug(figure.rect)
        # TODO у фигуры хранить координаты

    def display_figures(self, mirror=False):
        # TODO Сделать возможность зеркального отображения
        self.draw_cells()
        desk = self.get_desk()
        for figure in desk[np.where(desk)]:
            self.__draw_figure(figure)


desk = VisualDesk()
screen.blit(desk, (50, 20))


def main():
    clock = pg.time.Clock()
    while True:
        pg.display.update()
        clock.tick(60)
        # Проходим по всем произошедшим событиям
        for event in pg.event.get():
            # Если нажат крестик, выходим из цикла
            if event.type == pg.QUIT:
                return


if __name__ == "__main__":
    main()
