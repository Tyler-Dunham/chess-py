import math

class King():

    def __init__(self, cur_pos, inCheck):
        self.cur_pos = cur_pos
        self.inCheck = inCheck

    def Move(self, new_pos):
        
        cx, cy = self.cur_pos
        nx, ny = new_pos

        if (
            nx not in range(1, 9) #Check column bounds
            or ny not in range(1, 9) #Check row bounds
            or (nx == cx and ny == cy) #Same move
            or abs(nx - cx) > 1  
            or abs(ny - cy) > 1
            ):
            print("Invalid move.")
            return
        
        self.cur_pos = new_pos
        print("Moved.")