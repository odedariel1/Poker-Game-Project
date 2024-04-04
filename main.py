from Classes.Board import Board

a=Board()
a.set_players()
print(a.players)
a.players[0].bet()
a.players[1].bet()
a.start_game()
