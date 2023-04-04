import pygame as pg
from desk import Desk
import numpy as np
from loguru import logger
from icecream import ic
logger.enable('chess_figures')


img_path = "./src/img/"
pg.init()
screen = pg.display.set_mode((1200, 700))

cell_size = 80


class VisualDesk(Desk, pg.Surface):
    def __init__(self, pos):
        Desk.__init__(self, size=cell_size)
        pg.Surface.__init__(self, [cell_size*8]*2)
        self.rect = self.get_rect(
            center=[cell_size*4+pos[0], cell_size*4+pos[1]])
        # Выбраная фигура
        self.__select_figure = None
        self.display_figures()

    def draw_cells(self):
        colors = ('#eceed2', '#759455')
        for row in range(8):
            for col in range(8):
                pg.draw.rect(self, colors[(row+col) % 2],
                             (row*cell_size, col*cell_size,
                              cell_size, cell_size))

    def __draw_figure(self, figure):

        self.blit(figure.image, figure.rect)
        # TODO у фигуры хранить координаты

    def display_figures(self, mirror=False):
        # TODO Сделать возможность зеркального отображения
        self.draw_cells()
        desk = self.get_desk()
        for figure in desk[np.where(desk)]:
            self.__draw_figure(figure)

    def click(self, pos):
        desk = self.get_desk()
        for figure in desk[np.where(desk)]:
            if figure.rect.collidepoint(*pos):
                ic(figure)
                if not self.__select_figure:
                    self.__select_figure = figure
        else:
            self.__select_figure = False


def main():
    left, top = 20, 50
    desk = VisualDesk((left, top))
    screen.blit(desk, (left, top))
    clock = pg.time.Clock()
    while True:
        pg.display.update()
        clock.tick(60)
        # Проходим по всем произошедшим событиям
        for event in pg.event.get():
            # Если нажат крестик, выходим из цикла
            if event.type == pg.QUIT:
                return
            if event.type == pg.MOUSEBUTTONUP:
                if desk.rect.collidepoint(*event.pos):
                    x = event.pos[0] - left
                    y = event.pos[1] - top
                    desk.click((x, y))


if __name__ == "__main__":
    main()
