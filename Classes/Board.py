from Classes.Card import Card
from Classes.Player import Player
import random
class Board:
    def __init__(self):
        create_cards_pack = lambda: [Card(number, sign) for number in range(2, 15) for sign in ["♥", "♦", "♣", "♠"]]
        self.all_cards = create_cards_pack()
        self.on_board_cards = []
        self.total_bet = 0
        self.new_bet = 0
        self.players = []
        self.folded_players = []
    def set_players(self):
        players_amount = int(input("how many players: "))
        while 2 > players_amount or 4 < players_amount:
            print("you need at list 2 players to play and no more then 4")
            players_amount = int(input("how many players: "))

        count = 1
        while count <= players_amount:
            name = input(f"Enter {count} Player Name: ")
            if name is not None and len(name) > 1:
                self.players.append(Player(count, name))
                count += 1

    def player_action(self):
        count = 0
        while count < len(self.players) > 1:
            for index in range(len(self.players)):
                print(f"total bet: {self.total_bet}")
                action = int(input(f"Player {self.players[index].userid} 1. Check  2. fold  3. Bet : "))
                while action == "" or 3 < action < 0:
                    print("something went wrong")
                    action = int(input(f"Player {self.players[index].userid} 1. Check  2. fold  3. Bet : "))

                if action == 1 and self.new_bet == 0:
                    self.players[index].check()
                    count += 1

                elif action == 1 and self.new_bet != 0:
                    self.players[index].call(self.new_bet)
                    self.total_bet += self.new_bet
                    count += 1
                    print(count)
                    if count >= len(self.players):
                        print("reset work")
                        self.new_bet = 0
                        break

                elif action == 2:
                    self.players[index].fold()
                    self.folded_players.append(self.players.pop(self.players[index].userid-1))
                    index -= 1
                    if count >= len(self.players):
                        self.new_bet = 0
                        break
                    if len(self.players) == 1:
                        print(f"{self.players} won the round")  # winner
                        break

                elif action == 3:
                    temp_new_bet = self.players[index].bet(self.new_bet)
                    while temp_new_bet is None:
                        temp_new_bet = self.players[index].bet(self.new_bet)
                    if self.new_bet < temp_new_bet:
                        self.new_bet = temp_new_bet
                        self.total_bet += temp_new_bet
                        count = 1
                    else:
                        count += 1
    def open_table_cards(self):  # this function manage on table cards
        if len(self.on_board_cards) == 5:
            self.all_cards.extend(self.on_board_cards)
            self.on_board_cards = []
        if len(self.players) > 1:
            if len(self.on_board_cards) == 0:
                self.on_board_cards.append(self.all_cards.pop())
                self.on_board_cards.append(self.all_cards.pop())
                self.on_board_cards.append(self.all_cards.pop())
            else:
                self.on_board_cards.append(self.all_cards.pop())

            print(self.on_board_cards)

    def find_winner(self):
            if self.players == 1:
                print(f"The Winner is {self.players}")
                self.players[0].collect_cash(self.total_bet)
                self.total_bet = 0
                self.new_bet = 0
            elif len(self.on_board_cards) == 5:
                highestscore = 0
                for player in self.players:
                    score = player.cards + self.on_board_cards
            else:
                return self.open_table_cards()

    def find_pairs(self, cards):
        all_cards = {}
        for card in reversed(cards):
            if card.number not in all_cards:
                all_cards[card.number] = 1
            else:
                all_cards[card.number] += 1
        print(all_cards)
        print(max(all_cards.items(), key=lambda x: x[1]))

    def calculate_score(self, player, cards):
        #score = player.cards + self.on_board_cards
        score = cards
        score = sorted(score, key=lambda x: x.number)
        # result = self.find_pairs(score)
        # return "Royal Flash"
        # return "Straight Flush"
        #if self.find_pairs(score) == 4:
        #   return "Four of Kind"
        #if self.find_pairs(score) == 5:
            #return "Full House"
        # return "Flush"
        # return "Straight"
        #if self.find_pairs(score) == 3:
            #return "Three of Kind"
        #if self.find_pairs(score) == 2:
            #return "Two Pair"
        if self.find_pairs(score) == 1:
            return "One Pair"
        if max((card.number for card in cards)):
            return {"High Card": max((card.number for card in cards))}
        count = 0
        pass

    def start_game(self):
        # while len(self.players) > 1:
        while 0 < len(self.folded_players):
            self.players.append(self.folded_players.pop())

        random.shuffle(self.all_cards)  # suffle Game Cards
        for player in self.players:
            if player.cash == 0:
                    self.players.remove(player)
                    print(f"Player {player.userid} lost the game")

            player.set_cards([self.all_cards.pop(), self.all_cards.pop()])  # set cards to all players
            print(player, player.open_cards())
            print(self.players)

        print(self.all_cards)
        self.player_action()  # start round 1
        self.open_table_cards()
        self.player_action()  # start round 2
        self.open_table_cards()
        self.player_action()  # start round 3
        self.open_table_cards()
        # open last card and find a winner.
        # return all cards to the main pack
        # check if someone lost all cash
        # start over