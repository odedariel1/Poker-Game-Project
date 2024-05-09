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
        success = False
        while not success:
            try:
                players_amount = int(input("how many players: "))
                if 2 > players_amount or 4 < players_amount:
                    print("you need at list 2 players to play and no more then 4")
                else:
                    success = True
            except ValueError:
                print("Cant insert string or empty string please try again with numbers")

        count = 1
        while count <= players_amount:
            name = input(f"Enter {count} Player Name: ")
            if name is not None and len(name) > 1:
                self.players.append(Player(count, name))
                count += 1

    def action_input(self, index):
        return int(input(f"Player {self.players[index].userid} 1. Check  2. fold  3. Bet : "))

    def player_action(self):
        count = 0
        while count < len(self.players) > 1:
            index = 0
            max_index = len(self.players)
            while index < max_index:
                print(f"total bet: {self.total_bet}")
                success = False
                while not success:
                    try:
                        action = self.action_input(index)
                        if 3 < action or action <= 0:
                            print("you need to choose a number between 1 to 3")
                        else:
                            success = True
                    except ValueError:
                        print("Cant insert string or empty string please try again with numbers")

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
                for i in range(0, 3):
                    self.on_board_cards.append(self.all_cards.pop())
            else:
                self.on_board_cards.append(self.all_cards.pop())
            print(self.on_board_cards)

    def find_winner(self):
            if len(self.on_board_cards) == 5:
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

    def compare_scores(self, player1, player2, score1, score2):
        if score1[0] == score2[0]:
            if score1[1] > score2[1]:
                return player1, score1
            elif score1[1] < score2[1]:
                return [player2], score2
            else:
                player1.append(player2)
                return player1, score1
        if score1[0] == "Royal Flush":
            return player1, score1[0]
        elif score2[0] == "Royal Flush":
            return [player2], score2[0]
        elif score1[0] == "Straight Flush":
            return player1, score1[0]
        elif score2[0] == "Straight Flush":
            return [player2], score2[0]
        elif score1[0] == "Four of Kind":
            return player1, score1[0]
        elif score2[0] == "Four of Kind":
            return [player2], score2[0]
        elif score1[0] == "Full House":
            return player1, score1[0]
        elif score2[0] == "Full House":
            return [player2], score2[0]
        elif score1[0] == "Three of Kind":
            return player1, score1[0]
        elif score2[0] == "Three of Kind":
            return [player2], score2[0]
        elif score1[0] == "Two Pair":
            return player1, score1[0]
        elif score2[0] == "Two Pair":
            return [player2], score2[0]
        elif score1[0] == "One Pair":
            return player1, score1[0]
        elif score2[0] == "One Pair":
            return [player2], score2[0]
        elif score1[0] == "High Card":
            return player1, score1[0]
        elif score2[0] == "High Card":
            return [player2], score2[0]

    def is_royal_flush(self, cards):
        # Check if the hand is a royal flush
        royal_flush_values = set([10, 11, 12, 13, 14])
        return self.is_straight_flush(cards) and royal_flush_values.issubset(set([card.number for card in cards])), 14

    def is_straight_flush(self, cards):
        # Check if the hand is a straight flush
        return self.is_straight(cards)[0] and self.is_flush(cards)[0], self.is_straight(cards)[1]

    def is_four_of_a_kind(self, cards):
        # Check if the hand is four of a kind
        card_values = [card.number for card in cards]
        for value in card_values:
            if card_values.count(value) == 4:
                return True, value
        return False, 0

    def is_full_house(self, cards):
        # Check if the hand is a full house
        full_house = False
        max_sol = 0
        if self.is_three_of_a_kind(cards)[0] and self.is_one_pair(cards)[0]:
            max_sol = max(self.is_three_of_a_kind(cards)[1], self.is_one_pair(cards)[1])
            full_house = True
        return full_house, max_sol

    def is_flush(self, cards):
        # Check if the hand is a flush
        suits = sorted([card.sign for card in cards])
        for card in suits:
            if suits.count(card) >= 5:
                return True, max([x.number for x in cards if card == x.sign])
        return False, 0

    def is_straight(self, cards):
        # Check if the hand is a straight
        card_values = sorted([card.number for card in cards])
        index = 0
        while index <= 2:
            temp = list(range(card_values[index], card_values[len(card_values)+index-3]))
            index += 1
            if set(temp).issubset(set(card_values)):
                return True, max(temp)
        return False, 0

    def is_three_of_a_kind(self, cards):
        # Check if the hand is three of a kind
        card_values = [card.number for card in cards]
        for value in card_values:
            if card_values.count(value) == 3:
                return True, value
        return False, 0

    def is_two_pair(self, cards):
        # Check if the hand is two pair
        pair_count = 0
        card_values = [card.number for card in cards]
        max_value = 0
        for value in set(card_values):
            if card_values.count(value) == 2:
                pair_count += 1
                if max_value <= value:
                    max_value = value
        return pair_count == 2, value

    def is_one_pair(self, cards):
        # Check if the hand is one pair
        pair_count = 0
        card_values = [card.number for card in cards]
        for value in set(card_values):
            if card_values.count(value) == 2:
                return True, value
        return False, 0

    def calculate_score(self, cards):
        all_cards = sorted(cards, key=lambda card: card.number)
        if self.is_royal_flush(all_cards)[0]:
            return ["Royal Flush", 14]
        elif self.is_straight_flush(all_cards)[0]:
            return ["Straight Flush", self.is_straight_flush(all_cards)[1]]
        elif self.is_four_of_a_kind(all_cards)[0]:
            return ["Four of Kind", self.is_four_of_a_kind(all_cards)[1]]
        elif self.is_full_house(all_cards)[0]:
            return ["Full House", self.is_full_house(all_cards)[1]]
        elif self.is_flush(all_cards)[0]:
            return ["Flush", self.is_flush(all_cards)[1]]
        elif self.is_straight(all_cards)[0]:
            return ["Straight", self.is_straight(all_cards)[1]]
        elif self.is_three_of_a_kind(all_cards)[0]:
            return ["Three of Kind", self.is_three_of_a_kind(all_cards)[1]]
        elif self.is_two_pair(all_cards)[0]:
            return ["Two Pair", self.is_two_pair(all_cards)[1]]
        elif self.is_one_pair(all_cards)[0]:
            return ["One Pair", self.is_one_pair(all_cards)[1]]
        else:
            return "High Card", all_cards[-1]

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
            self.open_table_cards()
            self.player_action()  # start round 3
            self.open_table_cards()
            self.find_winner()  # find a winner.
            self.set_new_match()  # return all folded players/used cards to the game and kick who lost all cash
        else:
            print("Game Ended")
