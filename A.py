class TheGreatPileUp:

    piles = 0
    cards = []
    iterations = 0
    result = []

    def __init__(self):
        self.read_input()
        print(self.process_piles(self.cards))

    def read_input(self):
        self.piles = input()
        self.cards = [int(i) for i in raw_input().split(' ')]

    def process_piles(self, cards):
        l = len(cards)
        result = []
        if l % 2 == 0:
            for i in range(l / 2):
                merged = cards[0: 2 * i] + [cards[2 * i] + cards[2 * i + 1]] + cards[2 * i + 1:]
                if merged == sum(cards):
                    return (1, "TRIVIAL MERGE")
                if merged == merged[::-1]:
                    return (1, merged)
        return (1, "TRIVIAL MERGE")

if __name__ == '__main__':
    TheGreatPileUp()
