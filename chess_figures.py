from abc import abstractmethod
import json
from loguru import logger

logger.disable("chess_figures")

with open("./src/img/symbols.json", encoding="utf-8") as f:
    _str_images = json.load(f)


def _validate_moves(moves: list) -> list:
    cells = [[gate for gate in move
             if min(gate) >= 0 and max(gate) <= 7] for move in moves]
    return [cell for cell in cells if cell]

# Фигуры: pawn, rook, knight, king, queen, bishop


class Figure:
    name = ""
    eng_name = ""
    notation_name = ""
    price = 0

    def __init__(self, color: bool):
        '''
        Цвет задается при создании
        белый = True
        '''
        self.color = color

    def get_color(self):
        return self.color*2-1

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
    notation_name = "P"
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
    notation_name = "N"
    price = 3

    def possible_moves(self, coords: list) -> list:
        # TODO Прописать все коды у коня
        return _validate_moves([[coords[0] + 1, coords[1] + 2],
                                [coords[0] + 2, coords[1] - 1],
                                [coords[0] - 1, coords[1] - 2],
                                [coords[0]-2, coords[1] + 1]])

    def possible_takes(self, coords: list) -> list:
        return self.possible_moves(coords)


class Rook(Figure):
    name = "Башня"
    eng_name = "Rook"
    notation_name = "R"
    price = 5


class Bishop(Figure):
    name = "Слон"
    eng_name = "Bishop"
    notation_name = "B"
    price = 3


class Queen(Figure):
    name = "Королева"
    eng_name = "Queen"
    notation_name = "Q"
    price = 8


class King(Figure):
    name = "Король"
    eng_name = "King"
    notation_name = "K"
    price = 0


NOTATION = {
    "P": Pawn,
    "R": Rook,
    "N": Knight,
    "B": Bishop,
    "K": King,
    "Q": Queen,
}

VOID = Void()

if __name__ == "__main__":
    ...
    P = Pawn(color=False)
    print(P.possible_takes([6, 0]))
    # N = Knight(color=True)
    # print(N.possible_moves([6, 1]))
    # print(N)
    # print(a.possible_takes([6, 0]))
