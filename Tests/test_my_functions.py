import pytest
from Classes.Board import Board
from Classes.Card import Card
from Classes.Player import Player

main = Board()
main.players = [Player(1, 'oded'),Player(2, "Dor")]
def test_set_cards_to_players():
    main.set_cards_to_players()
    assert len(main.players[0].cards) > 0 and len(main.players[1].cards)

def test_open_table_cards_round_1():
    main.open_table_cards()
    assert len(main.on_board_cards) == 3

def test_find_winner_round_2():  # just open another card
    main.find_winner()
    assert len(main.on_board_cards) == 4

def test_find_winner_round_3():
    main.players[0].cards = [Card(2,"♥"),Card(4, "♦")] # "♣", "♠", "♦", "♥"
    main.players[1].cards = [Card(14, "♥"), Card(14, "♦")]
    main.on_board_cards = [Card(9, "♥"), Card(7, "♦"), Card(14, "♣"), Card(14, "♠")]
    main.find_winner()
    assert len(main.on_board_cards) == 5 and main.winner_test[0].userid == main.players[1].userid

def test_is_royal_flush():
    cards = [Card(10, "♥"), Card(11, "♥"), Card(12, "♥"), Card(13, "♥"), Card(14, "♥"), Card(2, "♣"), Card(3, "♣")]
    assert main.is_royal_flush(cards)

def test_is_straight_flush():
    cards = [Card(7, "♥"), Card(6, "♥"), Card(4, "♥"), Card(5, "♥"), Card(6, "♥"), Card(7, "♥"), Card(8, "♥")]
    assert main.is_straight_flush(cards)

def test_is_four_of_a_kind():
    cards = [Card(2, "♥"), Card(2, "♦"), Card(14, "♣"), Card(2, "♠"), Card(9, "♠"), Card(11, "♣"), Card(2, "♣")]
    assert main.is_four_of_a_kind(cards)

def test_is_full_house():
    cards = [Card(2, "♥"), Card(2, "♦"), Card(14, "♣"), Card(14, "♠"), Card(9, "♠"), Card(11, "♣"), Card(2, "♣")]
    assert main.is_full_house(cards)

def test_is_flush():
    cards = [Card(7, "♦"), Card(3, "♥"), Card(4, "♥"), Card(5, "♥"), Card(6, "♦"), Card(11, "♥"), Card(10, "♥")]
    assert main.is_flush(cards)

def test_is_straight():
    cards = [Card(2, "♥"), Card(3, "♦"), Card(4, "♣"), Card(5, "♠"), Card(6, "♠"), Card(7, "♣"), Card(8, "♣")]
    assert main.is_straight(cards)

def test_is_three_of_a_kind():
    cards = [Card(9, "♥"), Card(9, "♦"), Card(14, "♣"), Card(14, "♠"), Card(9, "♠"), Card(7, "♣"), Card(5, "♣")]
    assert main.is_three_of_a_kind(cards)

def test_is_two_pair():
    cards = [Card(7, "♥"), Card(9, "♦"), Card(14, "♣"), Card(14, "♠"), Card(2, "♠"), Card(7, "♣"), Card(5, "♣")]
    assert main.is_two_pair(cards)

def test_is_one_pair():
    cards = [Card(2, "♥"), Card(7, "♦"), Card(14, "♣"), Card(14, "♠"), Card(9, "♠"), Card(11, "♣"), Card(5, "♣")]
    assert main.is_one_pair(cards)
