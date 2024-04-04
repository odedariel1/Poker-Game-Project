
class Player:
    def __init__(self, userid, name):
        self.userid = userid
        self.name = name
        self.cash = 1000
        self.cards = []

    def __repr__(self):
        return f'player {self.userid} name:{self.name} Current Cash:{self.cash}\n'

    def __str__(self):
        return f'player {self.userid}\n name:{self.name}\n Current Cash:{self.cash}'

    def set_cards(self, cards):
        self.cards = cards

    def open_cards(self):
        return f'1st Card:{self.cards[0]}, 2nd Card:{self.cards[1]}'

    def bet(self, input_amount):
            if self.cash >= input_amount:
                self.cash -= input_amount
                print(f'Player:{self}\n Bet :{input_amount}')
            else:
                print("Invalid Amount of Bet")

            pass


 #   def bet(self, input_amount):
  #      try:
  #      if self.cash >= input_amount:
   #         self.cash-=input_amount
   #         print(f'Player:{self}/n Bet :{input_amount}')
  #      else:
  #          raise customException("Invalid Amount of Bet")
   #     except customException:
   #         print("Exception Occured: ")
