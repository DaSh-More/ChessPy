from abc import abstractmethod
import json
from loguru import logger
from pathlib import Path
import pygame as pg


logger.disable("chess_figures")

img_path = "./src/img/"

with open("./src/img/symbols.json", encoding="utf-8") as f:
    _str_images = json.load(f)


def _validate_moves(moves: list) -> list:
    cells = [[place for place in move
             if min(place) >= 0 and max(place) <= 7] for move in moves]
    return [cell for cell in cells if cell]

# Фигуры: pawn, rook, knight, king, queen, bishop


class Figure(pg.sprite.Sprite):
    name = ""
    eng_name = ""
    notation_name = ""
    price = 0

    def __init__(self, color: bool, size=None):
        '''
        Цвет задается при создании
        белый = True
        '''
        super().__init__()
        self.color = color
        self.coords = [0, 0]
        self.size = size
        logger.debug(size)
        if pg.mixer.get_init():
            self.pg_init()

    def pg_init(self):
        self.image = pg.image.load(
            self.get_image()).convert_alpha()
        if self.size:
            self.image = pg.transform.scale(self.image,
                                            (self.size, self.size))

    @property
    def rect(self):
        return self.image.get_rect(
            center=(self.coords[1]*self.size + self.size/2,
                    self.size*8-self.coords[0]*self.size - self.size/2))

    def get_color(self):
        return self.color*2-1

    def get_image(self):
        return Path(img_path) / f"{'bw'[self.color]}{self.notation_name}.png"

    @abstractmethod
    def possible_moves(self, coords: list) -> list:
        """
        Принимает координаты фигуры, возвращает список,
            гда каждый элемент это список ходов


        Args:
            coords (list): Позиция фигуры [row, column]

        Returns:
            list: Возможные ходы [[row, column], [row, column], ...]
        """

    # TODO Реализовать по умолчанию
    @abstractmethod
    def possible_takes(self, coords: list) -> list:
        """
        Принимает координаты фигуры, возвращает список,
            гда каждый элемент это список ходов со съедением


        Args:
            coords (list): Позиция фигуры [row, column]

        Returns:
            list: Возможные ходы [[row, column], [row, column], ...]
        """

    def __str__(self):
        """
        Текстовое представление фигуры

        Returns:
            str: UTF-8 изображение фигуры
        """
        return _str_images.get(self.notation_name, "  ")[self.color]

    def __repr__(self):
        return f"<Figure.{self.eng_name}.{('Black', 'White')[self.color]}>"

    def __bool__(self):
        return True


class Void:
    color = None
    notation_name = ' '

    def __repr__(self):
        return ' '

    def __bool__(self):
        return False


class Pawn(Figure):
    name = "Пешка"
    eng_name = "Pawn"
    notation_name = "p"
    price = 1

    def possible_moves(self, coords: list) -> list:
        # Проходим от до 1 (+1 если на первой линии)
        # Добавляя 1 если белый иначе отнимая
        moves = [[coords[0]+(1+i)*self.get_color(), coords[1]]
                 for i in range(1 + (coords[0] in (1, 6)))]
        return _validate_moves([moves])

    def possible_takes(self, coords: list) -> list:
        return _validate_moves([[[coords[0] + self.get_color(),
                                  coords[1] - 1]],
                                [[coords[0] + self.get_color(),
                                  coords[1] + 1]]])


class Knight(Figure):
    name = "Конь"
    eng_name = "Knight"
    notation_name = "n"
    price = 3

    def possible_moves(self, coords: list) -> list:
        return _validate_moves([[[coords[0] + i, coords[1] + j]]
                                for i in (-2, -1, 1, 2)
                                for j in (-2, -1, 1, 2)
                                if abs(i-j) in (3, 1)])

    def possible_takes(self, coords: list) -> list:
        return self.possible_moves(coords)


class Rook(Figure):
    name = "Башня"
    eng_name = "Rook"
    notation_name = "r"
    price = 5

    def possible_moves(self, coords: list) -> list:
        return _validate_moves([[[coords[0] + i, coords[1]] for i in range(1, 8)],
                                [[coords[0] - i, coords[1]]
                                    for i in range(1, 8)],
                                [[coords[0], coords[1] + i]
                                    for i in range(1, 8)],
                                [[coords[0], coords[1] - i] for i in range(1, 8)]])

    def possible_takes(self, coords: list) -> list:
        return self.possible_moves(coords)


class Bishop(Figure):
    name = "Слон"
    eng_name = "Bishop"
    notation_name = "b"
    price = 3

    def possible_moves(self, coords: list) -> list:
        return _validate_moves([[[coords[0] + i, coords[1] + i] for i in range(1, 8)],
                                [[coords[0] - i, coords[1] - i]
                                    for i in range(1, 8)],
                                [[coords[0] + i, coords[1] - i]
                                    for i in range(1, 8)],
                                [[coords[0] - i, coords[1] + i] for i in range(1, 8)]])

    def possible_takes(self, coords: list) -> list:
        return self.possible_moves(coords)


class Queen(Figure):
    name = "Ферзь"
    eng_name = "Queen"
    notation_name = "q"
    price = 8

    def possible_moves(self, coords: list) -> list:
        return Rook.possible_moves(self, coords) + Bishop.possible_moves(self, coords)

    def possible_takes(self, coords: list) -> list:
        return self.possible_moves(coords)


class King(Figure):
    name = "Король"
    eng_name = "King"
    notation_name = "k"
    price = 0

    def possible_moves(self, coords: list) -> list:
        return _validate_moves([[[coords[0] + i, coords[1] + j]]
                                for i in (-1, 0, 1)
                                for j in (-1, 0, 1)
                                if not (i == 0 and j == 0)])

    def possible_takes(self, coords: list) -> list:
        return self.possible_moves(coords)


NOTATION = {
    "p": Pawn,
    "r": Rook,
    "n": Knight,
    "b": Bishop,
    "k": King,
    "q": Queen,
}

VOID = Void()

if __name__ == "__main__":
    ...
    P = Pawn(color=False)
    print(P.possible_moves([6, 0]))
    N = Knight(color=True)
    # print(N.possible_moves([4, 4]))
    # K = King(color=True)
    # print(K.possible_moves([0, 5]))
    # R = Rook(color=True)
    # print(R.possible_moves([0,0]))
    # B = Bishop(color=True)
    # print(B.possible_moves([0, 0]))
    logger.disable("__main__")
    Q = Queen(color=True)
    # print(Q.possible_moves([7, 7]))
    print(Q.color)
