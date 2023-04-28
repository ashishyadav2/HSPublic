import random

class Puzzle:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    def display(self):
        print(self.state[0])
        print(self.state[1])
        print(self.state[2])
        print()
    
    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)
    
    def get_next_states(self):
        next_states = []
        blank_i, blank_j = self.get_blank_position()
        
        if blank_i > 0:
            next_state = [row[:] for row in self.state]
            next_state[blank_i][blank_j], next_state[blank_i - 1][blank_j] = \
            next_state[blank_i - 1][blank_j], next_state[blank_i][blank_j]
            next_states.append(Puzzle(next_state))
        
        if blank_i < 2:
            next_state = [row[:] for row in self.state]
            next_state[blank_i][blank_j], next_state[blank_i + 1][blank_j] = \
            next_state[blank_i + 1][blank_j], next_state[blank_i][blank_j]
            next_states.append(Puzzle(next_state))
        
        if blank_j > 0:
            next_state = [row[:] for row in self.state]
            next_state[blank_i][blank_j], next_state[blank_i][blank_j - 1] = \
            next_state[blank_i][blank_j - 1], next_state[blank_i][blank_j]
            next_states.append(Puzzle(next_state))
        
        if blank_j < 2:
            next_state = [row[:] for row in self.state]
            next_state[blank_i][blank_j], next_state[blank_i][blank_j + 1] = \
            next_state[blank_i][blank_j + 1], next_state[blank_i][blank_j]
            next_states.append(Puzzle(next_state))
        
        return next_states
    
    def heuristic(self):
        # number of tiles that are not in their goal position
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal[i][j]:
                    count += 1
        return count
    
    def is_goal(self):
        return self.state == self.goal

def hill_climbing(puzzle):
    current = puzzle
    
    while True:
        print("Current state:")
        current.display()
        
        if current.is_goal():
            break
        
        next_states = current.get_next_states()
        if not next_states:
            break
        
        next_states.sort(key=lambda x: x.heuristic())
        if next_states[0].heuristic() >= current.heuristic():
            break
        
        current = next_states[0]
    
    print("Goal state reached:")
    current.display()

# testing
puzzle = Puzzle([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
hill_climbing(puzzle)
