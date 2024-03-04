from random import randint

class Calculate:
    def __init__(self: object, difficulty: int, /) -> None:
        self.__difficulty: int = difficulty
        self.__value1: int = self._generate_value
        self.__value2: int = self._generate_value
        self.__operation: int = randint(1, 3)  # 1 = sum, 2 subtract, 3 multiply
        self.__result: int = self._generate_result



    @property
    def difficulty(self: object) -> int:
        return self.__difficulty

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object) -> int:
        return self.__value2

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
        op: str = ''
        if self.__operation == 1:
            op = 'Sum'
        elif self.__operation == 2:
            op = 'Subtract'
        elif self.__operation == 3:
            op = 'Multiply'
        else:
            op = 'operation not found'

        return f'Value 1: {self.value1} \nValue 2: {self.value2} \nDifficulty: {self.difficulty} \nOperation: {op}'

    @property
    def _generate_value(self: object) -> int:
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        else:
            return randint(0, 1000)
        self.check_generate()

    @property
    def _generate_result(self: object) -> int:
        # Generate the result of the operation based on the difficulty and operation type
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            print(self.value1, self.value2)
            return abs(self.value1 - self.value2)  # Use abs() to ensure a non-negative result

        else:
            return self.value1 * self.value2


    @property
    def _check_operation(self: object) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            self.check_generate()
            return '-'
        else:
            return 'x'

    def check_result(self: object, answer: int) -> int:
        correct: bool = False
        if self.result == answer:
            print('Right answer')
            correct = True
            return correct
        else:
            print('you missed')
            print(f'{self.value1} {self._check_operation} {self.value2} = {self.result}')
            return correct

    def show_operation(self: object) -> str:
         return f'{self.value1} {self._check_operation} {self.value2} = ?'

    def check_generate(self: object) -> None:
            while self.value2 > self.value1:
                self.__value2: int = self._generate_value
