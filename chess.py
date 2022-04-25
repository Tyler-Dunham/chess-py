from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from King import King
from Knight import Knight

#Pawns
wp1 = Pawn([1, 2], 1, "White")
wp2 = Pawn([2, 2], 1, "White")
wp3 = Pawn([3, 2], 1, "White")
wp4 = Pawn([4, 2], 1, "White")
wp5 = Pawn([5, 2], 1, "White")
wp6 = Pawn([6, 2], 1, "White")
wp7 = Pawn([7, 2], 1, "White")
wp8 = Pawn([8, 2], 1, "White")

bp1 = Pawn([1, 7], 1, "Black")
bp2 = Pawn([2, 7], 1, "Black")
bp3 = Pawn([3, 7], 1, "Black")
bp4 = Pawn([4, 7], 1, "Black")
bp5 = Pawn([5, 7], 1, "Black")
bp6 = Pawn([6, 7], 1, "Black")
bp7 = Pawn([7, 7], 1, "Black")
bp8 = Pawn([8, 7], 1, "Black")

#Rooks
wr1 = Rook([1, 1])
wr2 = Rook([8, 1])

br1 = Rook([1, 8])
br2 = Rook([8, 8])

#Bishops
wb1 = Bishop([3, 1])
wb2 = Bishop([6, 1])

bb1 = Bishop([3, 8])
bb2 = Bishop([6, 8])

#Knights
wn1 = Knight([5, 4])
wn2 = Knight([7, 1])

bn1 = Knight([2, 8])
bn2 = Knight([7, 8])

#Queens
wq = Queen([4, 1])
bq = Queen([4, 8])

#Kings
wk = King([5, 4], False)
bk = King([5, 8], False)

# Test game
# wp5.Move([5, 4])
# bp5.Move([5, 5])
# wn2.Move([6, 3])
# bn1.Move([3, 6])
# wp4.Move([4, 4])
# bb2.Move([2, 4])
# wb1.Move([4, 2])