from abc import abstractmethod


def existing_moves(moves: list) -> list:
    return [move for move in moves if (0 <= move[0] <= 7) and (0 <= move[1] <= 7)]

# Фигуры: pawn,rook,knight, king, queen, bishop


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
            return existing_moves([[cell[0] - 1, cell[1] - 1], [cell[0]-1, cell[1] + 1]])
        else:
            return existing_moves([[cell[0] + 1, cell[1] + 1], [cell[0] + 1, cell[1] - 1]])


class Knight(Figure):
    name = "Конь"
    eng_name = "Knight"
    notation_name = "N"
    price = 3

    def possible_moves(self, cell: list) -> list:
        return existing_moves([[cell[0] + 1, cell[1] + 2], [cell[0] + 2, cell[1] - 1], [cell[0] - 1, cell[1] - 2], [cell[0]-2, cell[1] + 1]])
    def possible_takes(self, cell: list) -> list:
        return self.possible_moves(cell)

if __name__ == "__main__":
    a = Pawn(color=True)
    b = Knight(color=True)
    print(b.possible_moves([6,1]))
    # print(a.possible_takes([6, 0]))
