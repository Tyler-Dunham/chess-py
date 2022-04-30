class Game():

    def __init__(self, turns, player_turn, isPlaying, board):
        self.player_turn = player_turn
        self.turns = turns
        self.isPlaying = isPlaying
        self.board = board

    def displayBoard(self):
        counter = 1
        board = self.board
        print()
        for idy, row in enumerate(board):
            for idx, place in enumerate(row):
                if type(place).__name__ != "int":
                    print(f"{place.color}{place.__class__.__name__}: [{idx+1, idy+1}]".center(25), end=" | ")
                else: 
                    print("Empty".center(25), end=" | ")
                if counter % 8 == 0:
                    print("\n")
                    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

                counter += 1

    def move_piece(self, piece, to):
        if piece.color != self.player_turn:
            print("It's not your turn!")
            return
        piece.Move(to)  



class Bishop():

    def __init__(self, cur_pos, color, img):
        self.cur_pos = cur_pos
        self.color = color
        self.img = img

    def Move(self, new_pos):

        cx, cy = self.cur_pos
        nx, ny = new_pos

        if (
            nx not in range(1, 9) #Check column bounds
            or ny not in range(1, 9) #Check row bounds
            or (nx == cx and ny == cy) #Same move
            or (abs(nx - cx) != abs(ny - cy))): #If movement is not diagonal
            print("Invalid move.")
            return
        
        move_on_board(self, new_pos)



class King():

    def __init__(self, cur_pos, inCheck, color, img):
        self.cur_pos = cur_pos
        self.inCheck = inCheck
        self.color = color
        self.img = img

    def Move(self, new_pos):
        
        cx, cy = self.cur_pos
        nx, ny = new_pos

        if (
            nx not in range(1, 9) #Check column bounds
            or ny not in range(1, 9) #Check row bounds
            or (nx == cx and ny == cy) #Same move
            or abs(nx - cx) > 1  
            or abs(ny - cy) > 1
            or self.inCheck == True
            ):
            print("Invalid move.")
            return
        
        move_on_board(self, new_pos)



class Knight():

    def __init__(self, cur_pos, color, img):
        self.cur_pos = cur_pos
        self.color = color
        self.img = img

    def Move(self, new_pos):

        cx, cy = self.cur_pos
        nx, ny = new_pos

        if (
            nx not in range(1, 9) #Check column bounds
            or ny not in range(1, 9) #Check row bounds
            or (nx == cx and ny == cy) #Same move
            or ((abs(nx - cx) != 1 or abs(ny - cy) != 2) and (abs(ny - cy) != 1 or abs(nx - cx) != 2)) #Check move logic
            ):
            print("Invalid move.")
            return

        move_on_board(self, new_pos)



class Queen():

    def __init__(self, cur_pos,color, img):
        self.cur_pos = cur_pos
        self.color = color
        self.img = img
    
    def Move(self, new_pos):

        cx, cy = self.cur_pos
        nx, ny = new_pos

        if (
            nx not in range(1, 9) #Check column bounds
            or ny not in range(1, 9) #Check row bounds
            or (nx == cx and ny == cy) #Same move
            or ((nx != cx and ny != cy) and (abs(nx - cx) != abs(ny - cy)))): #If movement is diagonal or horizontal
            print("Invalid move.")
            return
        
        move_on_board(self, new_pos)



class Pawn():
    
    def __init__(self, cur_pos, move_num, color, img):
        self.cur_pos = cur_pos
        self.move_num = move_num
        self.color = color
        self.img = img

    def Move(self, new_pos):

        cx, cy = self.cur_pos
        nx, ny = new_pos
        mn = self.move_num
        new_spot = game.board[ny-1][nx-1]

        #Promotion
        if self.color == "White" and ny == 1:
            move_on_board(self, new_pos)
            self = Queen([nx, ny], "White", "♛")
            move_on_board(self, new_pos)
            return
        elif self.color == "Black" and ny == 8:
            self = Queen([nx, ny], "Black", "♕")
            move_on_board(self, new_pos)
            return
 
        #Diag captures
        if abs(ny - cy) == 1 and abs(nx - cx) == 1:
            if type(new_spot).__name__ != "int" and new_spot.color != self.color:
                move_on_board(self, new_pos)
                return

        #Invalid move
        if (
            (mn != 1 and abs(ny - cy) != 1)
            or (mn == 1 and abs(ny - cy) not in range(1, 3))
            or (self.color == "Black" and cy > ny)
            or (self.color == "White" and cy < ny)
            or (cy == ny)
            or (cx != nx)
            ): 
            print("Invalid move.")
            return

        move_on_board(self, new_pos)



class Rook():

    def __init__(self, cur_pos, color, img):
        self.cur_pos = cur_pos
        self.color = color
        self.img = img
    
    def Move(self, new_pos):

        cx, cy = self.cur_pos
        nx, ny = new_pos
        
        if (
            nx not in range(1, 9) #Check column bounds
            or ny not in range(1, 9) #Check row bounds
            or (nx == cx and ny == cy) #Same move
            or (nx != cx and ny != cy)): #Check direction 
            print("Invalid move.")
            return
        
        move_on_board(self, new_pos)




#Pawns
wp1 = Pawn([1, 7], 1, "White", "♟")
wp2 = Pawn([2, 7], 1, "White", "♟")
wp3 = Pawn([3, 7], 1, "White", "♟")
wp4 = Pawn([4, 7], 1, "White", "♟")
wp5 = Pawn([5, 7], 1, "White", "♟")
wp6 = Pawn([6, 7], 1, "White", "♟")
wp7 = Pawn([7, 7], 1, "White", "♟")
wp8 = Pawn([8, 7], 1, "White", "♟")

bp1 = Pawn([1, 2], 1, "Black", "♙")
bp2 = Pawn([2, 2], 1, "Black", "♙")
bp3 = Pawn([3, 2], 1, "Black", "♙")
bp4 = Pawn([4, 2], 1, "Black", "♙")
bp5 = Pawn([5, 2], 1, "Black", "♙")
bp6 = Pawn([6, 2], 1, "Black", "♙")
bp7 = Pawn([7, 2], 1, "Black", "♙")
bp8 = Pawn([8, 2], 1, "Black", "♙")

#Rooks
wr1 = Rook([1, 8], "White", "♜")
wr2 = Rook([8, 8], "White", "♜")

br1 = Rook([1, 1], "Black", "♖")
br2 = Rook([8, 1], "Black", "♖")

#Bishops
wb1 = Bishop([3, 8], "White", "♝")
wb2 = Bishop([6, 8], "White", "♝")

bb1 = Bishop([3, 1], "Black", "♗")
bb2 = Bishop([6, 1], "Black", "♗")

#Knights
wn1 = Knight([2, 8], "White", "♞")
wn2 = Knight([7, 8], "White", "♞")

bn1 = Knight([2, 1], "Black", "♘")
bn2 = Knight([7, 1], "Black", "♘")

#Queens
wq = Queen([4, 8], "White", "♛")
bq = Queen([4, 1], "Black", "♕")

#Kings
wk = King([5, 8], False, "White", "♚")
bk = King([5, 1], False, "Black", "♔")

#Board
board = [[br1, bn1, bb1, bq, bk, bb2, bn2, br2],
        [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], 
        [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
        [wr1, wn1, wb1, wq, wk, wb2, wn2, wr2]]

game = Game(0, "White", True, board)

def move_on_board(piece, new_pos):
    x, y = new_pos
    cx, cy = piece.cur_pos

    if (type(game.board[y-1][x-1]).__name__ == "int" #Empty space
        or (type(game.board[y-1][x-1]).__name__ != "int" 
        and game.board[y-1][x-1].color != piece.color) #Self attack
        ):
        game.board[cy-1][cx-1] = 0
        piece.cur_pos = new_pos
        game.board[y-1][x-1] = piece
        game.turns += 1
        print(f"{piece.__class__.__name__} moved to {piece.cur_pos}. {game.player_turn}")

        if game.turns % 2 == 0:
            game.player_turn = "White"
            print(f"It is {game.player_turn}'s turn")
        else: 
            game.player_turn = "Black"
            print(f"It is {game.player_turn}'s turn")

        if wk.inCheck:
            print(f"White king in check!")
        elif bk.inCheck:
            print(f"Black king in check!")

    elif game.board[y-1][x-1].color == piece.color and (y == 8 or y == 1):
        game.board[cy-1][cx-1] = 0
        piece.cur_pos = new_pos
        game.board[y-1][x-1] = piece
        print(f"{piece.__class__.__name__} moved to {piece.cur_pos}. {game.player_turn}")

        if game.turns % 2 == 0:
            game.player_turn = "White"
            print(f"It is {game.player_turn}'s turn")
        else: 
            game.player_turn = "Black"
            print(f"It is {game.player_turn}'s turn")

        if wk.inCheck:
            print(f"White king in check!")
        elif bk.inCheck:
            print(f"Black king in check!")


    else:
        print(f"Your {game.board[y-1][x-1].__class__.__name__} is there!")