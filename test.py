from random import randint


class One:
    def __init__(self):
        print('One')


class Two:
    def __init__(self):
        print('Two')


di = {1: One, 2: Two}

random_class = di[randint(1, 2)]
r = random_class()
