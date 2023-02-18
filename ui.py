import pygame as pg
from desk import Desk
import numpy as np

img_path = "./src/img/"
pg.init()
# Задаем размер окна
screen = pg.display.set_mode((1200, 700))
# Создаем ообъект часов

# pg.draw.rect(screen,
#              (255, 255, 255),
#              (20, 20, 100, 75))


class VisualDesk(Desk, pg.Surface):
    def __init__(self):
        Desk.__init__(self)
        pg.Surface.__init__(self, (640, 640))

        self.display_figures()

    def draw_cells(self):
        colors = ('#759455', '#eceed2')
        for row in range(8):
            for col in range(8):
                pg.draw.rect(self, colors[(row+col) % 2],
                             (row*80, col*80, 80, 80))

    def draw_figure(self, figure, cords):
        # TODO Сделать все фигуры объектами для рисования
        # TODO у фигуры хранить координаты
        pg.draw.rect(self, colors[(row+col) % 2],
                     (row*80, col*80, 80, 80))

    def display_figures(self):
        self.draw_cells()
        print(np.where(self.get_desk()))


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
