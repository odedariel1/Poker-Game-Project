from Classes.Card import Card
from Classes.Player import Player
import random
class Board:
    def __init__(self):
        create_cards_pack = lambda: [Card(number, sign) for number in range(2, 15) for sign in ["♥", "♦", "♣", "♠"]]
        self.all_cards=create_cards_pack()
        self.on_board_cards=[]
        self.totalBet=0
        self.newBet=0
        self.players=[]

    def set_players(self):
        players_amount = int(input("how many players: "))
        while 2 > players_amount or 4 < players_amount:
            print("you need at list 2 players to play and no more then 4")
            players_amount = int(input("how many players: "))

        count=1
        while count <= players_amount:
            name = input(f"Enter {count} Player Name: ")
            if name is not None and len(name) > 1 :
                self.players.append(Player(count, name))
                count += 1

    def start_game(self):
        #while len(self.players) > 1 :
        random.shuffle(self.all_cards)  #suffle Game Cards
        for player in self.players:
            if player.cash == 0:
                    self.players.remove(player)

            player.set_cards([self.all_cards.pop(), self.all_cards.pop()]) #set cards to all players
            print(player, player.open_cards())
            print(self.players)

        print(self.all_cards)
        #start round1
        #...........

    def find_winner(self):
        return ""


