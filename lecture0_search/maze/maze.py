from collections import deque
import os


class Maze:
    def __init__(self, filename):
        # Grid representation of the maze (2D list)
        self.grid = []

        # Start and goal positions
        self.start = None
        self.goal = None

        # Load maze from file
        self.load_maze(filename)

    def load_maze(self, filename):
        # Read file line by line and convert into a 2D grid
        with open(filename, "r") as file:
            self.grid = [list(line.rstrip("\n")) for line in file]

        # Identify start (S) and goal (G) positions
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "S":
                    self.start = (i, j)
                elif self.grid[i][j] == "G":
                    self.goal = (i, j)

    def neighbors(self, state):
        # Extract current position
        i, j = state

        # Possible moves: up, down, left, right
        possible_moves = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1)
        ]

        valid_neighbors = []

        # Check each move
        for x, y in possible_moves:
            # Ensure the move is within grid boundaries
            if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[x]):
                # Ensure the cell is not a wall
                if self.grid[x][y] != "#":
                    valid_neighbors.append((x, y))

        return valid_neighbors

# ================= BFS =================
    def solve_with_exploration_bfs(self):
        # Queue for BFS (FIFO)
        queue = deque()
        # Add the start state to the queue
        queue.append((self.start, [self.start]))
        # Mark the start state as visited immediately
        visited = {self.start}
        # List to store order of explored nodes (for visualization)
        explored_order = []

        while queue:
            # Get first element from queue
            current_state, path = queue.popleft()

            # Store exploration order
            explored_order.append(current_state)

            # Check if goal reached
            if current_state == self.goal:
                return path, explored_order

            # Explore neighbors
            for neighbor in self.neighbors(current_state):
                if neighbor not in visited: # Add only nodes that were never seen before
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
                
        # If no solution found
        return None, explored_order
    
# ================= DFS =================
    def solve_with_exploration_dfs(self):
        # Stack for DFS (LIFO)
        stack = []
        # Add start state
        stack.append((self.start,[self.start]))
        # Mark start as visited immediately
        visited = {self.start}
        # List to store order of explored nodes
        explored_order = []

        while stack:
            # Get last element (LIFO)
            current_state, path = stack.pop()
            # Store exploration order
            explored_order.append(current_state)
            
            # Check if goal reached
            if current_state == self.goal:
                return path, explored_order
            
            # Explore neighbors
            for neighbor in self.neighbors(current_state):
                # Add only if not already discovered
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(( neighbor, path + [neighbor]))
            
        # If no solution found
        return None, explored_order

# ================= SIMPLE SOLVERS =================
    def solve_bfs(self):
        # BFS solution 
        path, _ = self.solve_with_exploration_bfs()
        return path
    
    def solve_dfs(self):
        # DFS solution
        path, _ = self.solve_with_exploration_dfs()
        return path


if __name__ == "__main__":
    # Get correct file path regardless of working directory
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "maze.txt")

    maze = Maze(file_path)
    
    print("BFS solution:")
    print(maze.solve_bfs())

    print("\nDFS solution:")
    print(maze.solve_dfs())