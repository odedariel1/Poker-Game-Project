from Classes.customException import customException
class Player:
    def __init__(self, userid, name):
        self.userid = userid
        self.name = name
        self.cash = 1000
        self.cards = []

    def __repr__(self):
        return f'Player {self.userid} name:{self.name} Current Cash:{self.cash}\n'

    def __str__(self):
        return f'Player {self.userid}\n name:{self.name}\n Current Cash:{self.cash}'

    def set_cards(self, cards):
        self.cards = cards

    def open_cards(self):
        return f'1st Card:{self.cards[0]}, 2nd Card:{self.cards[1]}'


    def bet(self):
        try:
            input_amount=int(input("Enter Bet Amount: "))
            if self.cash >= input_amount:
                self.cash-=input_amount
                print(f'{self}\n Bet :{input_amount}')
            else:
                raise customException("Invalid Amount of Bet")
        except customException as e:
            print("Exception Occured: ",e)
