from loguru import logger
from chess_figures import NOTATION, VOID
import numpy as np

# TODO Проверка что на начальной позиции не пересекаются поля
default_position = '00wr 01wn 02wb 03wq 04wk 05wb 06wn 07wr\
                    10wp 11wp 12wp 13wp 14wp 15wp 16wp 17wp\
                    60bp 61bp 62bp 63bp 64bp 65bp 66bp 67bp\
                    70br 71bn 72bb 73bq 74bk 75bb 76bn 77br'.split()

WHITE, BLACK = True, False


class Desk:
    def __init__(self, position=default_position, size=None):
        self.__desk = np.full((8, 8), VOID, dtype=object)
        self.__set_figures(position, size)
        self.__move_color = WHITE
        self.__taken_figures = []

    def taken_figures(self):
        return self.__taken_figures

    def move_color(self):
        return self.__move_color

    def get_desk(self):
        return self.__desk

    def __set_figures(self, positions, size):
        """
        Расставляет фигуры на доске

        Args:
            positions (list): Позиции фигур в формате
                {строка}{столбец}{цвет}{нотационное имя}
                00wr - белая тура на позиции a1
        """
        for fig in positions:
            fig = fig.lower()
            cords = list(map(int, fig[:2]))
            self.__desk[*cords] = NOTATION.get(fig[3])(fig[2] == 'w',
                                                       size=size)
            self.__desk[*cords].coords = cords

    def move(self, fromCoords: list, toCoords: list):
        # TODO Задать типы ошибок
        figure = self.__desk[*fromCoords]
        # Проверка на наличие фигуры
        if figure is VOID:
            raise TypeError('Empty cell')

        # Проверка на цвет фигуры
        if figure.color != self.__move_color:
            raise TypeError('Figure color')

        # Взятие или ход

        cells = figure.possible_moves(fromCoords)
        if to_figure := self.__desk[*toCoords]:
            if to_figure.color == figure.color:
                raise TypeError('take figure color error')
            cells = figure.possible_takes(fromCoords)

        # Проходим по возможным путям
        logger.debug(figure.__repr__())
        for path in cells:
            # Если поле есть на пути
            if toCoords in path:
                # Пройдем по всем полям списка
                for cell in path:
                    # Возьмем фигуру которая стоит на поле
                    cell_figure = self.__desk[*cell]
                    # Если мы дошли до нужного поля
                    if cell == toCoords:
                        # Если там стоит фигура этого же цвета
                        if figure.color == cell_figure.color:
                            raise TypeError('take figure color error')
                        self.__take(fromCoords, toCoords)
                        return True
                    # Иначе проверяем наличие фигуры
                    if cell_figure is not VOID:
                        return False
        else:
            raise TypeError('to cell error')

    def __take(self, fromCoords, toCoords):
        # Отмечаем фигуру как съеденую
        self.__taken_figures.append(self.__desk[*fromCoords])
        # Перемещаем ее
        self.__desk[*toCoords] = self.__desk[*fromCoords]
        self.__desk[*fromCoords] = VOID

        # Если после нашего хода нам шах, отменяем ход
        if self.__is_check(self.__move_color):
            self.__desk[*fromCoords] = self.__desk[*toCoords]
            self.__desk[*toCoords] = self.__taken_figures.pop()
        # Если шаха нет
        else:
            self.__move_color = not self.__move_color
            self.__desk[*toCoords].coords = toCoords

        # Удаляем из списка съеденых фигур пустое поле
        if self.__taken_figures[-1] is VOID:
            self.__taken_figures[-1].pop()

    def real_possible_moves(self, coords):
        figure = self.__desk[*coords]
        possible_moves = figure.possible_moves(coords)
        possible_takes = figure.possible_takes(coords)
        possible_takes_new = []
        for direction in possible_takes:
            for cell in direction:
                possible_takes_new.append(cell)
        real_possible_moves = []
        for direction in possible_moves:
            real_possible_moves.append([])
            for cell in direction:
                if self.__desk[*cell] is VOID:
                    real_possible_moves[-1].append(cell)
                elif self.__desk[*cell].color != figure.color:
                    if cell in possible_takes:
                        real_possible_moves[-1].append(cell)
                    break
                else:
                    break
        for _ in range(real_possible_moves.count([])):
            real_possible_moves.remove([])
        return real_possible_moves

    def __is_check(self, color=None):
        # TODO Сделать проверку на шах
        return False
        coords = []
        # for row in self.__desk:
        #     for figure in row:
        #         if (type(figure) == NOTATION['k']) and (figure.color == color):
        #             print('Yes')
        #             coords = [self.__desk.index(row), row.index(figure)]
        coords = self.__desk[(type(self.__desk[:, 1]) == NOTATION['k'])
                             & (self.__desk[:, 1].color == color)]
        return coords

    def is_check(self, color=None):
        return Desk.__is_check(self, color)

    def __repr__(self) -> str:
        field = '  a b c d e f g h\n'
        for n, i in enumerate(self.__desk[::-1]):
            field += f'{8-n} ' + ' '.join(map(str, i)) + '\n'
        return field[:-1]


if __name__ == "__main__":
    desk = Desk()
    # desk.move([1, 0], [2, 0])
    # desk.move([6, 0], [5, 0])
    # desk.move([0, 1], [2, 2])
    print(desk)
    print(desk.is_check(color=True))
