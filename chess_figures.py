from abc import abstractmethod
import json


with open("./src/img/symbols.json", encoding="utf-8") as f:
    _str_images = json.load(f)


def _existing_moves(moves: list) -> list:
    return [move for move in moves if min(move) >= 0 and max(move) <= 7]

# Фигуры: pawn, rook, knight, king, queen, bishop


class Figure:
    name = ""
    eng_name = ""
    notation_name = ""
    price = 0

    @abstractmethod
    def __init__(self, color: bool):
        '''
        Цвет задается при создании
        белый = True
        '''
        self.color = color

    @abstractmethod
    def possible_moves(self, cell: list) -> list:
        ...

    @abstractmethod
    def possible_takes(self, cell: list) -> list:
        ...

    @abstractmethod
    def __repr__(self):
        """
        Текстовое представление фигуры

        Returns:
            str: UTF-8 изображение фигуры
        """
        return _str_images.get(self.notation_name, "  ")[self.color]


class Void:
    color = False


class Pawn(Figure):
    name = "Пешка"
    eng_name = "Pawn"
    notation_name = "P"
    price = 1

    def possible_moves(self, cell: list) -> list:
        if cell[1] in (0, 7):
            return []
        if self.color:
            if cell[0] == 6:
                return [[cell[0] - 1, cell[1]], [cell[0] - 2, cell[1]]]
            else:
                return [[cell[0] - 1, cell[1]]]
        else:
            if cell[0] == 1:
                return [[cell[0] + 1, cell[1]], [cell[0] + 2, cell[1]]]
            else:
                return [[cell[0], cell[1]-1]]

    def possible_takes(self, cell: list) -> list:
        if self.color:
            return _existing_moves([[cell[0] - 1, cell[1] - 1], [cell[0]-1, cell[1] + 1]])
        else:
            return _existing_moves([[cell[0] + 1, cell[1] + 1], [cell[0] + 1, cell[1] - 1]])


class Knight(Figure):
    name = "Конь"
    eng_name = "Knight"
    notation_name = "N"
    price = 3

    def possible_moves(self, cell: list) -> list:
        return _existing_moves([[cell[0] + 1, cell[1] + 2],
                                [cell[0] + 2, cell[1] - 1],
                                [cell[0] - 1, cell[1] - 2],
                                [cell[0]-2, cell[1] + 1]])

    def possible_takes(self, cell: list) -> list:
        return self.possible_moves(cell)


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

if __name__ == "__main__":
    # P = Pawn(color=True)
    # N = Knight(color=True)
    # print(N.possible_moves([6, 1]))
    # print(N)
    # print(a.possible_takes([6, 0]))
