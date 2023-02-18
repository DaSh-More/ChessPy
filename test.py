class Test:
    def __init__(self) -> None:
        self.__t = 0


class A(Test):
    def __init__(self) -> None:
        super().__init__()


print(dir(A()))
