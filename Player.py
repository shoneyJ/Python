class Player:

    def __init__(self, name):
        self.myCards = []
        self.discardPile = []
        self.name = name

    def draw(self, card):
        self.myCards.append(card)

    def showTopCard(self):
        if(len(self.myCards) > 0):
            return self.myCards[0]
        else:
            return 'null'

    def win(self, card):
        self.discardPile.append(card)

    def lose(self):
        if(len(self.myCards) > 0):
            self.myCards.pop(0)

    def getRemainingCount(self):
        return len(self.myCards) + len(self.discardPile)

    def printPlaying(self):
        self.totalCards = len(self.myCards) + len(self.discardPile)
        s = '{} ({} cards):{}'.format(
            self.name, self.totalCards, self.showTopCard().get())
        print(s)

    def printRoundWinner(self):

        print('{} wins this round'.format(self.name))

    def printWinner(self):

        print('{} wins the game'.format(self.name))
