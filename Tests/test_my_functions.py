import pytest
from Classes.Board import Board
from Classes.Card import Card
from Classes.Player import Player


def test_set_cards_to_players():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    main.set_cards_to_players()
    assert len(main.players[0].cards) > 0 and len(main.players[1].cards)

def test_open_table_cards_round_1():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    main.open_table_cards()
    assert len(main.on_board_cards) == 3

def test_find_winner_round_2():  # just open another card
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    for i in range(0, 2):
        main.open_table_cards()
    assert len(main.on_board_cards) == 4

def test_find_winner_round_3():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    main.players[0].cards = [Card(2, "♥"),Card(4, "♦")]  # player 1
    main.players[1].cards = [Card(14, "♥"), Card(14, "♦")]  # player 2 The Winner!
    main.on_board_cards = [Card(9, "♥"), Card(7, "♦"), Card(3, "♦"), Card(14, "♣"), Card(14, "♠")]
    main.find_winner()
    assert len(main.on_board_cards) == 5 and main.winner_test[0].userid == main.players[1].userid

def test_is_royal_flush():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(10, "♥"), Card(11, "♥")]
    board_cards = [Card(12, "♥"), Card(13, "♥"), Card(14, "♥"), Card(2, "♣"), Card(3, "♣")]
    assert main.is_royal_flush(player_cards + board_cards)

def test_is_straight_flush():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(7, "♥"), Card(6, "♥")]
    board_cards = [Card(4, "♥"), Card(5, "♥"), Card(6, "♥"), Card(7, "♥"), Card(8, "♥")]
    assert main.is_straight_flush(player_cards + board_cards)[0]

def test_is_four_of_a_kind():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(2, "♥"), Card(2, "♦")]
    board_cards = [Card(14, "♣"), Card(2, "♠"), Card(9, "♠"), Card(11, "♣"), Card(2, "♣")]
    assert main.is_four_of_a_kind(player_cards + board_cards)[0]

def test_is_full_house():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(2, "♥"), Card(2, "♦")]
    board_cards = [Card(14, "♣"), Card(14, "♠"), Card(9, "♠"), Card(11, "♣"), Card(2, "♣")]
    assert main.is_full_house(player_cards + board_cards)[0]

def test_is_flush():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(7, "♦"), Card(3, "♥")]
    board_cards = [Card(4, "♥"), Card(5, "♥"), Card(6, "♦"), Card(11, "♥"), Card(10, "♥")]
    assert main.is_flush(player_cards + board_cards)[0]

def test_is_straight():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(2, "♥"), Card(3, "♦")]
    board_cards = [Card(4, "♣"), Card(5, "♠"), Card(6, "♠"), Card(11, "♣"), Card(12, "♣")]
    assert main.is_straight(player_cards + board_cards)[0]

def test_is_three_of_a_kind():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(9, "♥"), Card(9, "♦")]
    board_cards = [Card(14, "♣"), Card(14, "♠"), Card(9, "♠"), Card(7, "♣"), Card(5, "♣")]
    assert main.is_three_of_a_kind(player_cards + board_cards)[0]

def test_is_two_pair():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(7, "♥"), Card(9, "♦")]
    board_cards = [Card(14, "♣"), Card(14, "♠"), Card(2, "♠"), Card(7, "♣"), Card(5, "♣")]
    assert main.is_two_pair(player_cards + board_cards)[0]

def test_is_one_pair():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player_cards = [Card(2, "♥"), Card(7, "♦")]
    board_cards = [Card(14, "♣"), Card(14, "♠"), Card(9, "♠"), Card(11, "♣"), Card(5, "♣")]
    assert main.is_one_pair(player_cards + board_cards)[0]

def test_calculate_score():
    main = Board()
    main.players = [Player(1, 'oded'), Player(2, "Dor")]
    player1_cards = [Card(2, "♥"), Card(7, "♦")]  #Two Pair
    player2_cards = [Card(7, "♥"), Card(14, "♦")]  #Full House
    board_cards = [Card(7, "♥"), Card(3, "♠"), Card(14, "♣"), Card(14, "♠"), Card(9, "♦")]
    assert main.calculate_score(player1_cards + board_cards)[0] == "Two Pair" and\
           main.calculate_score(player2_cards + board_cards)[0] == "Full House"

