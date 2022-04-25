import math

class Knight():

    def __init__(self, cur_pos):
        self.cur_pos = cur_pos

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

        self.cur_pos = new_pos
        print("Moved.")