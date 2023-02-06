from abc import abstractmethod


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
    notation_name = ""
    price = 1

    def possible_moves(self, cell: list) -> list:
        if cell[1] in (0,7):
            return []
        if self.color:
            if cell[1] == 1:
                return [[cell[0], cell[1]+1], [cell[0], cell[1]+2]]
            else:
                return [[cell[0], cell[1]+1]]
        else:
            if cell[1] == 6:
                return [[cell[0], cell[1]-1], [cell[0], cell[1]-2]]
            else:
                return [[cell[0], cell[1]-1]]


a = Pawn(color=True)
print(a.possible_moves([1, 7]))
