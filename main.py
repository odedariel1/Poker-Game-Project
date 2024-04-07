from Classes.Board import Board
from Classes.Card import Card
a=Board()
a.set_players()
print(a.players)
# a.start_game()
cards = [Card(10, "♥"), Card(11, "♥"), Card(13, "♥"), Card(13, "♥"), Card(14, "♥"), Card(3, "♥"), Card(3, "♥")]
print(a.calculate_score(a.players[0], cards))