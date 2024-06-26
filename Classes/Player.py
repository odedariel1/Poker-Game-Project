from Classes.customException import customException
class Player:
    def __init__(self, userid, name):
        self.userid = userid
        self.name = name
        self.cash = 1000
        self.cards = []
        self.is_folded = False

    def __repr__(self):
        return f'Player {self.userid} name:{self.name} Current Cash:{self.cash}\n'

    def __str__(self):
        return f'Player {self.userid}\n name:{self.name}\n Current Cash:{self.cash}'

    def set_cards(self, cards):
        self.cards = cards

    def open_cards(self):
        return f'1st Card:{self.cards[0]}, 2nd Card:{self.cards[1]}'

    def check(self):
        print(f"Player {self.userid},{self.name} Checked")

    def fold(self):
        print(f"Player {self.userid},{self.name} Folded")

    def call(self, amount):
        if self.cash <= amount:
            amount, self.cash = self.cash, 0
            print(f"{self}\n Called :{amount}")
            return amount
        else:
            self.cash -= amount
            print(f'{self}\n Called :{amount}')
            return amount

    def player_input_bet(self):
        return int(input("Enter Bet Amount: "))

    def bet(self, oldbet):
        success = False
        while not success:
            try:
                input_amount = self.player_input_bet()
                if oldbet >= input_amount:
                    success = True
                    return self.call(oldbet)
                elif self.cash >= input_amount:
                    self.cash -= input_amount
                    print(f'{self}\n Bet :{input_amount}')
                    success = True
                    return input_amount
                else:
                    raise customException()
            except customException as e:
                print(f"Exception Occured: {e} Cash Left:{self.cash}")
            except ValueError:
                print("Cant insert string or empty string please try again with numbers")

    def collect_cash(self, amount):
        self.cash += amount
