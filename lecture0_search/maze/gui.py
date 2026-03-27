import tkinter as tk
import os
from maze import Maze

CELL_SIZE = 60  # Size of each cell in pixels


class MazeGUI:
    def __init__(self, root, maze):
        self.root = root
        self.maze = maze

        # Final solution path
        self.solution = None

        # Order of explored nodes (for animation)
        self.explored = []

        # Current animation step
        self.animation_index = 0

        # Prevent multiple animations at once
        self.is_animating = False

        self.root.title("Maze Solver - BFS")

        rows = len(self.maze.grid)
        cols = len(self.maze.grid[0])

        # Canvas where the maze is drawn
        self.canvas = tk.Canvas(
            root,
            width=cols * CELL_SIZE,
            height=rows * CELL_SIZE,
            bg="white"
        )
        self.canvas.pack(pady=10)

        # Buttons container
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Solve button
        self.solve_button = tk.Button(
            button_frame,
            text="Solve",
            command=self.start_animation
        )
        self.solve_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_maze
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Info label (path length and explored states)
        self.info_label = tk.Label(
            root,
            text="Path length: - | Explored states: -",
            font=("Arial", 12)
        )
        self.info_label.pack(pady=5)

        # Draw initial maze
        self.draw_maze()

    def get_cell_color(self, i, j):
        # Return color based on cell type
        cell = self.maze.grid[i][j]

        if cell == "#":
            return "black"
        if cell == "S":
            return "lime green"
        if cell == "G":
            return "red"
        return "white"

    def draw_maze(self):
        # Clear canvas
        self.canvas.delete("all")

        # Draw each cell
        for i in range(len(self.maze.grid)):
            for j in range(len(self.maze.grid[i])):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = self.get_cell_color(i, j)

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="light gray"
                )

    def draw_explored_cells(self, upto_index):
        # Draw explored nodes up to a certain animation step
        for k in range(upto_index):
            i, j = self.explored[k]

            # Skip start and goal cells
            if self.maze.grid[i][j] in ("S", "G"):
                continue

            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="light blue",
                outline="light gray"
            )

    def draw_solution(self):
        # Draw final path
        if self.solution is None:
            return

        for i, j in self.solution:
            if self.maze.grid[i][j] not in ("S", "G"):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill="gold",
                    outline="light gray"
                )

    def start_animation(self):
        # Prevent multiple animations running simultaneously
        if self.is_animating:
            return

        # Run BFS and get both solution and explored nodes
        self.solution, self.explored = self.maze.solve_with_exploration()

        self.animation_index = 0
        self.is_animating = True

        self.draw_maze()

        # Start animation loop
        self.animate_step()

    def animate_step(self):
        # Continue animation until all nodes are explored
        if self.animation_index <= len(self.explored):
            self.draw_maze()
            self.draw_explored_cells(self.animation_index)

            self.animation_index += 1

            # Call this function again after delay (milliseconds)
            self.root.after(150, self.animate_step)
        else:
            # Draw final result
            self.draw_maze()
            self.draw_explored_cells(len(self.explored))
            self.draw_solution()

            # Update statistics
            self.update_info()

            self.is_animating = False

    def update_info(self):
        # Compute path length and number of explored states
        path_length = len(self.solution) - 1 if self.solution else 0
        explored_count = len(self.explored)

        self.info_label.config(
            text=f"Path length: {path_length} | Explored states: {explored_count}"
        )

    def reset_maze(self):
        # Reset all state variables
        self.solution = None
        self.explored = []
        self.animation_index = 0
        self.is_animating = False

        # Redraw initial maze
        self.draw_maze()

        self.info_label.config(
            text="Path length: - | Explored states: -"
        )


if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "maze.txt")

    maze = Maze(file_path)

    root = tk.Tk()
    app = MazeGUI(root, maze)
    root.mainloop()