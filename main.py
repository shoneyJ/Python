from random import randint


class Card:

    def __init__(self, number):
        self.number = number

    def info(self):
        print(self.number)


# task 1 create a deck of card showing number 1 to 10
# each number is in the deck 4 times
deck = []
for times in range(0,4):
    for cardNum in range(1, 11):
        deck.append(Card(cardNum))


def shuffle(deck, n):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(n-1, 0, -1):
        # Pick a random index from 0 to i
        j = randint(0, i+1)

        # Swap arr[i] with the element at random index
        deck[i], deck[j] = deck[j], deck[i]



n = len(deck)

shuffle(deck, n)

for shuffledCard in deck:
    shuffledCard.info()

# end of task 1

# Draw cards.
    
