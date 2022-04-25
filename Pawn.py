class Pawn():
    
    def __init__(self, cur_pos, move_num, color):
        self.cur_pos = cur_pos
        self.move_num = move_num
        self.color = color

    def Move(self, new_pos):

        cx, cy = self.cur_pos
        nx, ny = new_pos
        mn = self.move_num

        if (
            nx != cx #Check column
            or ny == cy #Check row
            or (nx == cx and ny == cy) #Same move
            or ny not in range(1, 9) #Check bounds
            or (mn != 1 and abs(ny - cy) != 1) #Check move range after move 1
            or (mn == 1 and abs(ny - cy) not in range(1, 3)) #Check move range move 1
            or (self.color == "White" and ny < cy) #Check white move direction 
            or (self.color == "Black" and ny > cy)): #Check black move direction
            print("Invalid move.")
            return

        self.cur_pos = new_pos
        self.move_num += 1
        print(f"{__name__} moved to {self.cur_pos}.")