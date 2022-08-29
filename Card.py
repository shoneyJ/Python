class Card:

    def __init__(self, number):
        self.number = number

    def info(self):
        print(self.number, end=" ")

    def get(self):
        return self.number
