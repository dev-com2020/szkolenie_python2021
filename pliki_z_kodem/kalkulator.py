class BasicCalculator:

    def __init__(self):
        self.numbers = []
        self.signs = []
        self.result = 0

    def provide_number(self, number):
        self.numbers.append(number)
        if len(self.signs) == 0:
            self.result = number
        else:
            self.result = self.__calculate()

    def provide_operand(self, operand):
        self.signs.append(operand)

    def __calculate(self):
        if self.signs[-1] is '+':
            return self.result + self.numbers[-1]
        if self.signs[-1] is '-':
            return self.result + self.numbers[-1]
        if self.signs[-1] is '*':
            return self.result + self.numbers[-1]
        if self.signs[-1] is '/':
            return self.result + self.numbers[-1]

    def show_result(self):
        self.signs.append('=')
        sequence = ''
        for i in range(len(self.numbers)):
            sequence = sequence + '{} {}'.format(self.numbers[i], self.signs[i])
        sequence += str(self.result)
        print(sequence)
        return self.result, sequence
