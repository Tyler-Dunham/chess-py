class Rook():

    def __init__(self, cur_pos):
        self.cur_pos = cur_pos
    
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
        
        self.cur_pos = new_pos
        print(f"{__name__} moved to {self.cur_pos}.")