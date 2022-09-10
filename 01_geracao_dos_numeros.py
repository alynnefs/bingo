import random


def selecionar_numeros():
    return [
        random.sample(range(1, 16), 5),
        random.sample(range(16, 31), 5),
        random.sample(range(31, 46), 4),
        random.sample(range(46, 61), 5),
        random.sample(range(61, 76), 5),
    ]


print(selecionar_numeros())
