class Card:
        cardCount = 0
        colourNames = ['hearts', 'diamonds', 'spades', 'clubs']
        valueNames = ['ace', '2', '3', '4', '5', '6','7', '8', '9', 'knight', 'queen', 'king']

        def __init__ (self, colour, value):
                self.colour = colour
                self.value = value

        @classmethod
        def getColourName(cls, colour):
                return cls.colourNames[colour];

        @classmethod
        def getValueName(cls, value):
                return cls.valueNames[value];

        def toString(self):
                return Card.getValueName(self.value) + ' of ' + Card.getColourName(self.colour)
