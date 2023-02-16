import numpy as np
from chess_figures import NOTATION

default_position = '00wr 01wn 02wb 03wq 04wk 05wb 06wn 07wr\
                    60br 61bn 62bb 63bq 64bk 65bb 66bn 67br'.split()


class Desk:
    def __init__(self, position=default_position) -> None:
        self.desk = np.full((8, 8), ' ', dtype=object)
        self.set_figures(position)

    def set_figures(self, positions):
        for fig in positions:
            fig = fig.upper()
            cords = list(map(int, fig[:2]))
            self.desk[*cords] = NOTATION.get(fig[3])(fig[2] == 'W')

    def __repr__(self) -> str:
        field = ''
        for i in self.desk[::-1]:
            field += ' '.join(map(str, i)) + '\n'
        return field


if __name__ == "__main__":
    desk = Desk()
    print(desk)
