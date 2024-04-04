from Classes.Card import Card
from Classes.Player import Player
class Board:
    def __init__(self):
        create_cards_pack = lambda: [Card(number, sign) for number in range(2, 15) for sign in ["♥", "♦", "♣", "♠"]]
        self.allCards=create_cards_pack()
        self.onBoardCards=[]
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
                self.players.append(Player(count,name))
                count+=1

