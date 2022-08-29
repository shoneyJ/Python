import asyncio
from random import randint

from Card import Card
from Player import Player


async def shuffle(deck, n):
    print("Shuffling the deck")
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    for i in range(n-1, 0, -1):
        # Pick a random index from 0 to i
        j = randint(0, i+1)

    # Swap arr[i] with the element at random index
        deck[i], deck[j] = deck[j], deck[i]
        await asyncio.sleep(0.5)

    return deck


async def createDeck():
    print("Creating deck of cards")
    deck = []
    for cardNum in range(1, 11):
        deck.append(Card(cardNum))
        deck.append(Card(cardNum))
        deck.append(Card(cardNum))
        deck.append(Card(cardNum))

    await asyncio.sleep(5)
    return deck


async def drawCardForPlayer(player1, player2, deck):
    print("Distributing cards to player")
    n = len(deck)
    tempdeck = deck
    while n > 0:
        player1.draw(tempdeck[0])
        tempdeck.pop(0)
        player2.draw(tempdeck[0])
        tempdeck.pop(0)
        n = n-2
    await asyncio.sleep(5)


async def play(player1, player2, playCard1, playCard2):

    if(playCard1 > playCard2):
        player1.win(player2.showTopCard())
        player2.lose()
        player1.printRoundWinner()

    elif(playCard1 < playCard2):
        player2.win(player1.showTopCard())
        player1.lose()
        player2.printRoundWinner()
    elif(playCard1 == playCard2):
        return 'Tie'

    await asyncio.sleep(2)


async def onTie():
    print("To do")


async def main():
    # task 1 create a deck of card showing number 1 to 10
    # each number is in the deck 4 times
    task1 = asyncio.create_task(createDeck())
    newDeck = await task1
    n = len(newDeck)
    task2 = asyncio.create_task(shuffle(newDeck, n))
    shuffledDeck = await task2

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    task3 = asyncio.create_task(
        drawCardForPlayer(player1, player2, shuffledDeck))
    await task3

    while player1.showTopCard() != 'null' or player2.showTopCard() != 'null':

        wasTie = False
        if hasattr(player1.showTopCard(), 'get'):
            playCard1 = player1.showTopCard().get()

        else:
            player2.printWinner()
            break

        if hasattr(player2.showTopCard(), 'get'):
            playCard2 = player2.showTopCard().get()
        else:
            player1.printWinner()
            break

        if(player1.showTopCard() != 'null' and player2.showTopCard() != 'null'):
            player1.printPlaying()
            player2.printPlaying()

        task4 = asyncio.create_task(
            play(player1, player2, playCard1, playCard2))

        value = await task4

        if(value == 'Tie'):
            wasTie = True
            player1.lose()
            player2.lose()

        print(value)

        # print ('player one cards {}'.format(player1.showTopCard()))
        # print ('player two cards {}'.format(player2.showTopCard()))

        # else:
        #     print (player1.showTopCard())


asyncio.run(main())
# Draw cards.
