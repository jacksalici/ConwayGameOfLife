class Board:
    def __init__(self, width = 25, height = 10):
        self.char_dead = '·'
        self.char_alive = 'o'
        
        self.width = width
        self.height = height
        
        self.board = [[self.char_dead for _ in range(self.width)] for _ in range(self.height)]
    
        self.n_iterations = 0
        
        self.reset()
        
    def print_board(self):
        print(f"Iteration: {self.n_iterations}")
        for row in self.board:
            print(''.join(row))
            
    def get_alive_neighbours(self, x, y):
        alive_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= x + i < self.width) or not (0 <= y + j < self.height):
                    continue
                if self.board[y + j][x + i] == self.char_alive:
                    alive_count += 1
        return alive_count
    
    def reset(self, number_of_alive_cells=50):
        import random
        
        alive_idx = random.sample(range(self.width * self.height), number_of_alive_cells)
        
        for id in alive_idx:
            x = id % self.width
            y = id // self.width
            assert 0 <= x < self.width and 0 <= y < self.height, "Initial alive cell out of bounds"
            self.board[y][x] = self.char_alive
        
        self.n_iterations = 0
            
    def step(self):
        new_board = self.board.copy()
        
        for y in range(self.height):
            for x in range(self.width):
                alive_neighbours = self.get_alive_neighbours(x, y)
                
                if self.board[y][x] == self.char_alive:
                    if alive_neighbours < 2 or alive_neighbours > 3:
                        new_board[y][x] = self.char_dead
                else:
                    if alive_neighbours == 3:
                        new_board[y][x] = self.char_alive
        
        self.board = new_board
        self.n_iterations += 1
        
        
if __name__ == "__main__":
    board = Board()
    
    input("Press enter to start. Type 'r' to reset, or 'q' to quit.")
    
    while True:
        board.print_board()
        
        key = input().lower()
        
        if key.startswith('r'):
            board.reset(number_of_alive_cells = ''.join(filter(str.isdigit, key)) or 50)
        elif key == 'q':
            break
        else:
            board.step()
        