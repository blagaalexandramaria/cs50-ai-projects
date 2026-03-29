import copy

X = "X"
O = "O"
EMPTY = None
def initial_state():
    # Create and return an empty 3x3 board
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    # Determine whose turn it based on the number of moves made
    x_count = 0
    o_count = 0

    # Count how many X and O are on the board
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    # if count are equal: X plays (first player)
    if x_count == o_count:
        return X
    return O

def actions(board):
    # Generate all posible valid moves (empty cells)
    possible_actions = set()

    # Iterate through all cells of the board
    for i in range(3):
        for j in range(3):
            # If cell is empty: valid action
            if board[i][j] is EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions

def result(board, action):
   # Return a new board after applying a move
   # Do not modify the original board
    i,j = action

    # Validate action
    if action not in actions(board):
        raise Exception("Invalid action")
    
    # Create a deep copy to preserve original state
    new_board = copy.deepcopy(board)
    # Apply move for current_player
    new_board[i][j] = player(board)

    return new_board

def winner(board):
    # Check all possible winning lines (row, columns, diagonals)
    lines = []

    # Add rows
    for row in board:
        lines.append(row)
    
    # Add columns
    for j in range(3):
        column = [board[0][j], board[1][j], board[2][j]]
        lines.append(column)

    # Add diagonals
    lines.append([board [0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    # Check each line for winner
    for line in lines:
        if line == [X, X, X]:
            return X
        if line == [O, O, O]:
            return O
    
    return None

def terminal(board):
   # Check if game is finished

   # Case 1: someone has won
    if winner(board) is not None:
        return True
    
    # Case 2: no empty cells left: draw
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True

def utility(board):
    # Assign numeric value to terminal state
    game_winner = winner(board)

    # X wants to maximze: +1
    if game_winner == X:
        return 1
    # O wants to minimize: -1
    elif game_winner == O:
        return -1
    
    # Draw: neutral
    return 0

def minimax(board):
    # Return the optimal move using Minimax algorithm

    # If game already ended: no moves
    if terminal(board):
        return None
    
    current_player = player(board)
    
    # Max player (X)
    if current_player == X:
        best_value = float("-inf")
        best_action = None

        # Explore all possible actions
        for action in actions(board):
            # Simulate move and evaluate opponent response
            value = min_value(result(board, action))
            
            # Choose action with maximum value
            if value > best_value:
                best_value = value
                best_action = action
        
        return best_action

    # MIN player (O)
    else:
        best_value = float("inf")
        best_action = None

        # Explore all possible actions
        for action in actions(board):
            # Simulate move and evaluate opponent response
            value = max_value(result(board, action))

            # Choose action with minimum value
            if value < best_value:
                best_value = value
                best_action = action
        
        return best_action

def max_value(board):
    # Compute the maximum utility achievable from this state

    # Base case: terminal state
    if terminal(board):
        return utility(board)
    
    v = float("-inf")

    # Try all possible actions
    for action in actions(board):
        # Assume opponent plays optimal (minimizes)
        v = max(v, min_value(result(board, action)))
    
    return v

def min_value(board):
   # compute the minium utility achievable from this state

   # Base state: terminal case
    if terminal(board):
        return utility(board)
    
    v = float("inf")

    # Try all possible cases
    for action in actions(board):
        # Assume opponent plays optimally
        v = min(v, max_value(result(board, action)))

    return v

