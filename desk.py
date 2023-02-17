import numpy as np
from chess_figures import NOTATION, VOID

default_position = '00wr 01wn 02wb 03wq 04wk 05wb 06wn 07wr\
                    10wp 11wp 12wp 13wp 14wp 15wp 16wp 17wp\
                    60bp 61bp 62bp 63bp 64bp 65bp 66bp 67bp\
                    70br 71bn 72bb 73bq 74bk 75bb 76bn 77br'.split()

WHITE, BLACK = True, False


class Desk:
    def __init__(self, position=default_position):
        self.__desk = np.full((8, 8), VOID, dtype=object)
        self.__set_figures(position)
        self.__move_color = WHITE
        self.__taken_figures = []

    def taken_figures(self):
        return self.__taken_figures

    def move_color(self):
        return self.__move_color

    def __set_figures(self, positions):
        """
        Расставляет фигуры на доске

        Args:
            positions (list): Позиции фигур в формате
                {строка}{столбец}{цвет}{нотационное имя}
                00wr - белая тура на позиции a1
        """
        for fig in positions:
            fig = fig.upper()
            cords = list(map(int, fig[:2]))
            self.__desk[*cords] = NOTATION.get(fig[3])(fig[2] == 'W')

    def move(self, fromCoords, toCoords):
        figure = self.__desk[*fromCoords]
        # Проверка на наличие фигуры
        if figure is VOID:
            raise TypeError('Empty cell')

        # Проверка на цвет фигуры
        if figure.color != self.__move_color:
            raise TypeError('Figure color')

        # Проходим по возможным путям
        print(figure.__repr__(), toCoords, figure.possible_moves(fromCoords))
        for path in figure.possible_moves(fromCoords):
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
                    # Если мы не дошли до нужного поля, проверяем наличие фигуры
                    if cell_figure.color is not VOID:
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
        if self.__is_shah(self.__move_color):
            self.__desk[*fromCoords] = self.__desk[*toCoords]
            self.__desk[*toCoords] = self.__taken_figures.pop()
        else:
            self.__move_color = not self.__move_color

        # Удаляем из списка съеденых фигур пустое поле
        if self.__taken_figures[-1] is VOID:
            self.__taken_figures[-1].pop()

    def __is_check(self, color=None):
        ...

    def __repr__(self) -> str:
        field = ''
        for i in self.__desk[::-1]:
            field += ' '.join(map(str, i)) + '\n'
        return field.strip()


if __name__ == "__main__":
    desk = Desk()
    print(desk.move([1, 0], [2, 0]))
    print(desk)
