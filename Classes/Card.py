class Card:
    def __init__(self, number, sign):
        self.number=number
        self.sign=sign
        self.high_symbols= ('J', 'Q', 'K', 'A')

    def __repr__(self):
        if self.number > 10: return f'Card: {self.high_symbols[self.number-11]} {self.sign}'
        else: return f'Card: {self.number} {self.sign}'

    def __str__(self):
        if self.number > 10:
            return f'Card: {self.high_symbols[self.number - 11]} {self.sign}'
        else:
            return f'Card: {self.number} {self.sign}'

