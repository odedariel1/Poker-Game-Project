from Classes.Card import Card
from Classes.Player import Player
from Classes.decorator import _decorator
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
        self.winner_test = []

    @_decorator
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
            index = 0
            max_index = len(self.players)
            while index < max_index:  # on fold cause problems
                print(f"total bet: {self.total_bet}")
                action = int(input(f"Player {self.players[index].userid} 1. Check  2. fold  3. Bet : "))
                while action == "" or 3 < action or action < 0:
                    print("something went wrong")
                    action = int(input(f"Player {self.players[index].userid} 1. Check  2. fold  3. Bet : "))

                if action == 1 and self.new_bet == 0:
                    self.players[index].check()
                    index += 1
                    count += 1

                elif action == 1 and self.new_bet != 0:
                    call_bet = self.players[index].call(self.new_bet)
                    self.total_bet += call_bet
                    index += 1
                    count += 1

                    if count >= len(self.players):
                        self.new_bet = 0
                        break

                elif action == 2:
                    self.players[index].fold()
                    self.folded_players.append(self.players.pop(index))
                    max_index -= 1
                    if len(self.players) == 1:
                        self.players[0].collect_cash(self.total_bet)
                        print(f"The Winner is {self.players} ,total earn:{self.total_bet}")
                        self.total_bet = 0
                        self.new_bet = 0
                        break

                    if count >= len(self.players):
                        self.new_bet = 0
                        break

                elif action == 3:
                    temp_new_bet = self.players[index].bet(self.new_bet)
                    index += 1
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
            if len(self.on_board_cards) == 4:
                self.open_table_cards()
                winners_score = self.calculate_score(self.players[0].cards + self.on_board_cards)
                winners_players = [self.players[0]]
                for i in range(1, len(self.players)):
                    score = self.calculate_score(self.players[i].cards + self.on_board_cards)
                    winners_players, winners_score = self.compare_scores(winners_players, self.players[i], winners_score, score)

                print(f"{winners_score} , winners: {winners_players}")
                self.winner_test = winners_players
                for player in winners_players:
                    earn_cash = self.total_bet/len(winners_players)
                    player.collect_cash(earn_cash)
                    print(f"The Winner is {player} ,total earn:{earn_cash}")
                    self.total_bet = 0
                    self.new_bet = 0
                    print(f"Player {player.userid}, {player.open_cards()}")
            else:
                return self.open_table_cards()

    def compare_scores(self, player1, player2, score1, score2):
        if score1 == score2:  # need to improve this one!!
            higher1 = max(player1[0].cards[0].number, player1[0].cards[1].number)
            higher2 = max(player2.cards[0].number, player2.cards[1].number)
            if higher1 > higher2:
                return player1, score1
            elif higher1 < higher2:
                return [player2], score2
            else:
                player1.append(player2)
                return player1, score1
        if score1 == "Royal Flush":
            return player1, score1
        elif score2 == "Royal Flush":
            return [player2], score2
        elif score1 == "Straight Flush":
            return player1, score1
        elif score2 == "Straight Flush":
            return [player2], score2
        elif score1 == "Four of Kind":
            return player1, score1
        elif score2 == "Four of Kind":
            return [player2], score2
        elif score1 == "Full House":
            return player1, score1
        elif score2 == "Full House":
            return [player2], score2
        elif score1 == "Three of Kind":
            return player1, score1
        elif score2 == "Three of Kind":
            return [player2], score2
        elif score1 == "Two Pair":
            return player1, score1
        elif score2 == "Two Pair":
            return [player2], score2
        elif score1 == "One Pair":
            return player1, score1
        elif score2 == "One Pair":
            return [player2], score2
        elif score1 == "High Card":
            return player1, score1
        elif score2 == "High Card":
            return [player2], score2

    def is_royal_flush(self, cards):
        # Check if the hand is a royal flush
        royal_flush_values = set([10, 11, 12, 13, 14])
        return self.is_straight_flush(cards) and royal_flush_values.issubset(set([card.number for card in cards]))

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
        suits = sorted([card.sign for card in cards])
        for card in suits:
            if suits.count(card) >= 5:
                return True
        return False

    def is_straight(self, cards):
        # Check if the hand is a straight
        card_values = sorted([card.number for card in cards])
        index = 0
        while index < 2:
            temp = list(range(card_values[index], card_values[len(card_values)+index-3]))
            index += 1
            if set(temp).issubset(set(card_values)):
                return True
        return False

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
            return "Royal Flush"
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

    def set_new_match(self):
        while 0 < len(self.folded_players):
            self.players.append(self.folded_players.pop())
        self.players = sorted(self.players, key=lambda p: p.userid)
        index = 0
        max_index = len(self.players)
        while index < max_index:
            if len(self.players[index].cards) > 0:
                self.all_cards += self.players[index].cards  # return all cards to the pocket
                self.players[index].cards = []
            if self.players[index].cash == 0:
                self.players.pop(index)  # pop if player lost all his cash last round
                max_index -= 1
            else:
                index += 1

    def set_cards_to_players(self):
        for player in self.players:
            player.set_cards([self.all_cards.pop(), self.all_cards.pop()])  # set cards to all players
            print(player, player.open_cards())

    def start_game(self):
        count = 1
        while len(self.players)+len(self.folded_players) > 1:
            print(f"Match {count}")
            count += 1
            random.shuffle(self.all_cards)  # shuffle Game Cards
            self.set_cards_to_players()
            self.player_action()  # start round 1
            self.open_table_cards()
            self.player_action()  # start round 2
            self.find_winner()
            self.player_action()  # start round 3
            self.find_winner()  # open last card and find a winner.
            self.set_new_match()  # return all folded players/used cards to the game and kick who lost all cash
        else:
            print("Game Ended")