class Rank:

    T = 0
    permutations = []
    result = 0

    def __init__(self):
        self.read_input()
        self.process_input()
        print(self.result)

    def read_input(self):
        self.T = input()
        self.permutations = [raw_input() for i in range(self.T)]
        print(self.T, self.permutations)

    def process_input(self):
        product = 1
        for permutation in self.permutations:
            perm = [int(i) for i in list(permutation)]
            product *= self.get_rank(perm)
        print(product % 23456)

    def get_rank(self, list):
        rank = 0
        for i, e in enumerate(list):
            below_list = [x for x in list if x < e and x not in list[:i]]
            rank += len(below_list) * self.factorial(9 - i)
        return rank + 1

    def factorial(self, n):
        if n < 1:
            return 1
        else:
            return n * self.factorial(n - 1)

if __name__ == '__main__':
    Rank()