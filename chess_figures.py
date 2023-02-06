from abc import abstractmethod


class Figure:
    color = ""
    name = ""
    eng_name = ""
    notation_name = ""
    short_notation_name = ""
    short_notation_name = ""
    price = 0

    @abstractmethod
    def __init__(self, color: bool):
        '''
        Цвет задается при создании
        '''

    @abstractmethod
    def possible_moves(cell: str) -> list:
        ...

    @abstractmethod
    def possible_takes(cell: str) -> list:
        ...
