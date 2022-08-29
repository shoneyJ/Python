class Player:

    def __init__(self):
        self.myCards = []

    def draw(self, card):
        self.myCards.append(card)

    def print(self):       
        for index in range(0, len(self.myCards)):
            print(self.myCards[index].info())
