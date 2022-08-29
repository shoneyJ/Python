from random import randint

from Card import Card
from Player import Player


def shuffle(deck, n):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(n-1, 0, -1):
        # Pick a random index from 0 to i
        j = randint(0, i+1)

    # Swap arr[i] with the element at random index
        deck[i], deck[j] = deck[j], deck[i]


def main():
    # task 1 create a deck of card showing number 1 to 10
    # each number is in the deck 4 times
    deck = []
    for cardNum in range(1, 11):
        deck.append(Card(cardNum))

    n = len(deck)
    shuffle(deck, n)


# each players receives 20 cards from shuffled.

    player1 = Player()

    player2 = Player()

    tempdeck = deck


    print ("deck info")
    for obj in deck:
        print (obj.info())

   
    while n > 0:
        player1.draw(tempdeck[0])
        tempdeck.pop(0)
        player2.draw(tempdeck[0])
        tempdeck.pop(0)
        n = n-2
        
    print ("player one info")
    player1.print()

    print ("player two info")
    player2.print()


main()
# Draw cards.
