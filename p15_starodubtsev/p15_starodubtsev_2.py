import itertools as itools
import random

class card:

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
    

    def __str__(self):
        return f'{self.num} {self.suit}'


    @staticmethod
    def list_to_cards(lst: list):
        result = []
        for i in lst:
            result.append(
                card(i[0], i[1])
            )
        return result


class card_generator:

    def __init__(self, count=52, randomize=False):

        assert count == 52 or count == 36, 'Incorrect card count'

        nums = ['A'] + [*range(count % 10, 11)] + ['J', 'Q', 'K']
        suits = ['diamonds', 'clubs', 'hearts', 'spades']

        self.available_cards = card.list_to_cards(
            itools.product(suits, nums)
        )

        if randomize: random.shuffle(self.available_cards)


    def __iter__(self):
        return iter(self.available_cards)


    def __next__(self):

        if len(self.available_cards) <= 0: raise StopIteration

        return self.available_cards.pop(0)


    def __len__(self):
        return len(self.available_cards)


TEST = True
if TEST:
    generator = card_generator()
    
    for _ in range(25):
        print(next(generator))