import tkinter as tk
from tictactoe import *

class TicTacToeGUI:
    def __init__(self, root):
        # Initialize main window
        self.root = root
        self.root.title("Tic Tac Toe")

        # Game state (board)
        self.board = initial_state()

        # Matrix of buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Create visual grid
        self.create_board()
    
    def create_board(self):
        # Create 3x3 grid of buttons
        for i in range(3):
            for j in range(3):

                # Create buttonn for each cell
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 40),
                    width=5,
                    height=2,

                    # When clicked: call make_move(i, j)
                    command=lambda i=i, j=j: self.make_move(i,j)
                )
                # Place button in grid layout
                button.grid(row=i, column=j)
                # Store reference to button
                self.buttons[i][j] = button
    
    def make_move(self, i, j):
        # Handle player move and AI response
        # Ignore move if:
        # - cell is already occupied
        # - game already ended
        if self.board[i][j] is not EMPTY or terminal(self.board):
            return
        
        # === Player move ===

        # Apply player move to board
        self.board = result(self.board, (i,j))

        # Update UI
        self.update_board()

        # Check if game ended after player move
        if terminal(self.board):
            self.end_game()
            return
        
        # === AI move ===

        # Compute best move using Minimax
        ai_move = minimax(self.board)

        # Apply AI move if exists
        if ai_move:
            self.board = result(self.board, ai_move)
            self.update_board()
        
        # check if game ended after AI move
        if terminal(self.board):
            self.end_game()
        
    def update_board(self):
        # Synchronize UI with current board state
        for i in range(3):
            for j in range(3):
                # Get value from board
                value = self.board[i][j]
                
                # Update button text
                # EMPTY: ""
                # X / O: shown
                self.buttons[i][j]["text"] = value if value else ""
    
    def end_game(self):
        # Determine game result and display message
        win = winner(self.board)

        # Assign message based on winner
        if win == X:
            message = "X wins"
        elif win == O:
            message = "O wins"
        else:
            message = "Draw"
        
        # Show result popup
        self.show_message(message)

    def show_message(self, message):
        # Create popup window for end-game message

        popup = tk.Toplevel()
        popup.title("Game Over")

        # Display message text
        label = tk.Label(popup, text=message, font=("Arial", 20))
        label.pack(pady=20)

        # Restart button: resets game
        button = tk.Button(popup, text="Restart", command=lambda: self.restart(popup))
        button.pack(pady=10)
        
    def restart(self, popup):

        # Reset game state and UI

        # Close popup
        popup.destroy()

        # Reset board state
        self.board = initial_state()

        # Refresh UI
        self.update_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
    