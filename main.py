from Classes.Player import Player
from Classes.Board import Board
p1 = Player(1, 'oded')
print(p1)
p1.bet(10)

a=Board()
a.set_players()
print(a.players)
