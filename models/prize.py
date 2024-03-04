class Prize:
    def __init__(self, level, correct, stop, wrong):
        self.__level: int = level
        self.__correct: int = correct
        self.__stop: int = stop
        self.__wrong: int = wrong

#
# List of prizes for hard difficulty
hard_prizes: Prize = [
Prize(1, 1000, 0, 0),
Prize(2, 2000, 1000, 500),
Prize(3, 3000, 2000, 1000),
Prize(4, 4000, 3000, 1500),
Prize(5, 5000, 4000, 2000),
Prize(6, 10000, 5000, 2500),
Prize(7, 20000, 10000, 5000),
Prize(8, 30000, 20000, 10000),
Prize(9, 40000, 30000, 15000),
Prize(10, 50000, 40000, 20000),
Prize(11, 100000, 50000, 25000),
Prize(12, 200000, 100000, 50000),
Prize(13, 300000, 200000, 100000),
Prize(14, 400000, 300000, 150000),
Prize(15, 500000, 400000, 200000),
Prize(16, 1000000, 500000, 0),
]

# List of prizes for medium difficulty
medium_prizes = [
Prize(1, 250, 0, 0),
Prize(2, 500, 250, 125),
Prize(3, 750, 500, 250),
Prize(4, 1000, 750, 375),
Prize(5, 1250, 1000, 500),
Prize(6, 2500, 1250, 625),
Prize(7, 5000, 2500, 1250),
Prize(8, 7500, 5000, 2500),
Prize(9, 10000, 7500, 3750),
Prize(10, 12500, 10000, 5000),
Prize(11, 25000, 12500, 6250),
Prize(12, 50000, 25000, 12500),
Prize(13, 75000, 50000, 25000),
Prize(14, 100000, 75000, 37500),
Prize(15, 125000, 100000, 50000),
Prize(16, 250000, 125000, 0),
]

# List of prizes for easy difficulty
easy_prizes = [
Prize(1, 125, 0, 0),
Prize(2, 250, 125, 62),
Prize(3, 375, 250, 125),
Prize(4, 500, 375, 187),
Prize(5, 625, 500, 250),
Prize(6, 1250, 625, 312),
Prize(7, 2500, 1250, 625),
Prize(8, 3750, 2500, 1250),
Prize(9, 5000, 3750, 1875),
Prize(10, 6250, 5000, 2500),
Prize(11, 12500, 6250, 3125),
Prize(12, 25000, 12500, 6250),
Prize(13, 37500, 25000, 12500),
Prize(14, 50000, 37500, 18750),
Prize(15, 62500, 50000, 25000),
Prize(16, 125000, 62500, 0)
]


def consult_prize(level: int, difficulty: int) -> Prize:
    if difficulty == 1:
       return  easy_prizes[level]
    elif difficulty == 2:
       return medium_prizes[level]
    else:
       return hard_prizes[level]


