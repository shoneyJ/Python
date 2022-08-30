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

    def showTopDiscardedCard(self):
        if(len(self.discardPile) > 0):
            return self.discardPile[0]
        else:
            return 'null'

    def win(self, card):
        self.discardPile.append(card)

    def lose(self):
        if(len(self.myCards) > 0):
            self.myCards.pop(0)

    def onTieWin(self, otherCard):
        self.myCards.append(self.discardPile.pop(0))
        self.myCards.append(otherCard)
    
    def onTieLoss(self, otherCard):
        self.myCards.remove(otherCard)
       

    def getRemainingCount(self):
        return len(self.myCards) + len(self.discardPile)

    def printPlaying(self):
        self.totalCards = len(self.myCards) + len(self.discardPile)
        s = '{} ({} cards):{}'.format(
            self.name, len(self.myCards), self.showTopCard().get())
        print(s)

    def printRoundWinner(self):

        print('{} wins this round'.format(self.name))

    def printWinner(self):

        print('{} wins the game'.format(self.name))
