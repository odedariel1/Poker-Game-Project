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
            for player in self.players:
                print(f"total bet: {self.total_bet}")
                action = int(input(f"Player {player.userid} 1. Check  2. fold  3. Bet : "))
                while action == "" or 3 < action < 0:
                    print("something went wrong")
                    action = int(input(f"Player {player.userid} 1. Check  2. fold  3. Bet : "))

                if action == 1 and self.new_bet == 0:
                    player.check()
                    count += 1

                elif action == 1 and self.new_bet != 0:
                    player.call(self.new_bet)
                    self.total_bet += self.new_bet
                    count += 1
                    print(count)
                    if count >= len(self.players):
                        self.new_bet = 0
                        break

                elif action == 2:
                    player.fold()
                    self.folded_players.append(self.players.pop(player.userid - 1))
                    if count >= len(self.players):
                        self.new_bet = 0
                        break
                    if len(self.players) == 1:
                        self.players[0].collect_cash(self.total_bet)
                        print(f"The Winner is {self.players} ,total earn:{self.total_bet}")
                        self.total_bet = 0
                        self.new_bet = 0
                        break

                elif action == 3:
                    temp_new_bet = player.bet(self.new_bet)
                    while temp_new_bet is None:
                        temp_new_bet = player.bet(self.new_bet)
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
            if len(self.on_board_cards) == 4:
                self.open_table_cards()
                max_score = ""
                for player in self.players:
                    score = player.cards + self.on_board_cards
                    max_score = self.calculate_score(score)
                    print(max_score)
            else:
                return self.open_table_cards()

    def compare_scores(self):
    def is_royal_flush(self, cards):
        # Check if the hand is a royal flush
        royal_flush_values = set([10, 11, 12, 13, 14])
        return self.is_straight_flush(cards) and set([card.number for card in cards]) == royal_flush_values

    def is_straight_flush(self, cards):
        # Check if the hand is a straight flush
        return self.is_straight(cards) and self.is_flush(cards)

    def is_four_of_a_kind(self, cards):
        # Check if the hand is four of a kind
        card_values = [card.number for card in cards]
        for value in card_values:
            if card_values.count(value) == 4:
                return True
        return False

    def is_full_house(self, cards):
        # Check if the hand is a full house
        return self.is_three_of_a_kind(cards) and self.is_one_pair(cards)

    def is_flush(self, cards):
        # Check if the hand is a flush
        suits = [card.sign for card in cards]
        return len(set(suits)) == 1

    def is_straight(self, cards):
        # Check if the hand is a straight
        card_values = sorted([card.number for card in cards])
        return card_values == list(range(card_values[0], card_values[-1] + 1))

    def is_three_of_a_kind(self, cards):
        # Check if the hand is three of a kind
        card_values = [card.number for card in cards]
        for value in card_values:
            if card_values.count(value) == 3:
                return True
        return False

    def is_two_pair(self, cards):
        # Check if the hand is two pair
        pair_count = 0
        card_values = [card.number for card in cards]
        for value in set(card_values):
            if card_values.count(value) == 2:
                pair_count += 1
        return pair_count == 2

    def is_one_pair(self, cards):
        # Check if the hand is one pair
        pair_count = 0
        card_values = [card.number for card in cards]
        for value in set(card_values):
            if card_values.count(value) == 2:
                return True
        return False

    def calculate_score(self, cards):
        all_cards = sorted(cards, key=lambda card: card.number)
        if self.is_royal_flush(all_cards):
            return "Royal Flash"
        elif self.is_straight_flush(all_cards):
            return "Straight Flush"
        elif self.is_four_of_a_kind(all_cards):
            return "Four of Kind"
        elif self.is_full_house(all_cards):
            return "Full House"
        elif self.is_flush(all_cards):
            return "Flush"
        elif self.is_straight(all_cards):
            return "Straight"
        elif self.is_three_of_a_kind(all_cards):
            return "Three of Kind"
        elif self.is_two_pair(all_cards):
            return "Two Pair"
        elif self.is_one_pair(all_cards):
            return "One Pair"
        else:
            return "High Card"

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

        self.player_action()  # start round 1
        self.open_table_cards()
        self.player_action()  # start round 2
        self.find_winner()
        self.player_action()  # start round 3
        self.find_winner()
        # open last card and find a winner.
        # return all cards to the main pack
        # check if someone lost all cash
        # start over