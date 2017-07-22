import math
class FibonacciRightTriangles:

    N = 0
    result = 0

    def __init__(self):
        self.read_input()
        self.process_input()
        print(self.result)

    def read_input(self):
        self.N = input()

    def process_input(self):
        #start fibonacci sequence
        got_FRAT = False
        FRAT_prev = 3
        FRAT = 5
        is_alternative = False
        while not got_FRAT:
            temp = FRAT
            FRAT += FRAT_prev
            FRAT_prev = temp
            if FRAT > self.N and FRAT % 2 == 1 and is_alternative:
                got_FRAT = True
            is_alternative = not is_alternative
        larget_side = math.ceil(2 / math.sqrt(5) * FRAT)
        even_side = larget_side
        if larget_side % 2 != 0:
            even_side = math.sqrt(FRAT * FRAT - larget_side * larget_side)
        i = 1
        factor_count = 0
        while i < even_side:
            if even_side % i == 0:
                factor_count += 1
            i += 1
        self.result = factor_count + 1


if __name__ == '__main__':
    FibonacciRightTriangles()