from Components import *

# Test game
game.move_piece(wp1, [1, 5])
game.move_piece(bp2, [2, 4])
game.move_piece(wp1, [2, 4])
game.move_piece(bp1, [1, 3])
game.move_piece(wp1, [1, 3])
game.move_piece(bp8, [8, 3])
game.move_piece(wp1, [1, 2])
game.move_piece(bp8, [8, 4])
game.move_piece(wp1, [2, 1])
game.move_piece(bp8, [8, 5])

game.displayBoard()