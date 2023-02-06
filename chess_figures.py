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
        '''
        self.color = color
    @abstractmethod
    def possible_moves(cell: str) -> list:
        ...

    @abstractmethod
    def possible_takes(cell: str) -> list:
        ...

class Pawn(Figure):
    name = "Пешка"
    eng_name = "Pawn"
    notation_name = ""
    price = 1
    
