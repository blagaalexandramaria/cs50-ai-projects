# 🎮 Tic Tac Toe AI with Minimax & Alpha-Beta Pruning (Adversarial Search Visualization)

This project implements an **Artificial Intelligence agent** that plays Tic Tac Toe optimally using the **Minimax algorithm with Alpha-Beta Pruning**, a fundamental concept in adversarial search.

It also includes a **graphical interface (Tkinter GUI)** that allows interaction with the AI in real time.

---

## 📌 Overview

The goal is to create an AI that can play Tic Tac Toe **perfectly**, assuming the opponent also plays optimally.

The AI uses:
- Full game-tree exploration
- Alpha-Beta Pruning optimization
- Recursive decision-making
- Optimal strategy selection

👉 As a result, **the AI can never be defeated** — the best outcome for the human player is a draw.

---

## 🧩 Problem Representation

The game is modeled as a **state-space search problem**:

- **State**: current configuration of the 3×3 board  
- **Players**: determines whose turn it is (X or O)  
- **Actions**: all valid moves (empty cells)  
- **Result(s, a)**: new board after applying action `a`  
- **Terminal(s)**: checks if the game is finished  
- **Utility(s)**:
  - `+1` → X wins  
  - `-1` → O wins  
  - `0` → draw  

---

## 🚀 Algorithm

### 🔵 Minimax

The Minimax algorithm simulates **all possible future game states** and selects the optimal move assuming both players play perfectly.

- **Max player (X)** → tries to maximize score  
- **Min player (O)** → tries to minimize score  

The algorithm works recursively:

- At each state:
  - Explore all possible actions
  - Simulate opponent's best response
  - Propagate values back up the tree

### 🟣 Alpha-Beta Pruning

To improve efficiency, the Minimax algorithm is optimized using **Alpha-Beta Pruning**.

This technique avoids exploring branches of the game tree that cannot influence the final decision.

- Reduces the number of states explored  
- Maintains the same optimal result  
- Improves performance without changing gameplay behavior  

---

### 🧠 Decision Rule

- X chooses the move with **maximum value**
- O chooses the move with **minimum value**

---

### ⚙️ Core Functions

- `max_value(state)` → best outcome for X  
- `min_value(state)` → best outcome for O  
- `minimax(state)` → returns optimal move  

---

## 🎨 GUI (Tkinter)

The project includes a simple graphical interface:

- Click on a cell → player move  
- AI responds instantly using Minimax  
- Game ends with a popup message  

---

## 🎮 Gameplay

- Player is always **X**
- AI is **O**
- Moves alternate automatically

👉 The AI:
- never makes mistakes  
- always chooses optimal moves  

---

## 🖼️ Example

### Initial State

|   |   |   |
|---|---|---|
|   |   |   |
|---|---|---|
|   |   |   |

### Mid Game

| X | O | X |
|---|---|---|
|   | O |   |
|---|---|---|
|   |   | X |

### Result
- Either **AI wins** or **draw**
- Human **cannot win**

---

## 🎬 How it works

1. Player clicks on a cell  
2. Move is applied using `result()`  
3. AI computes best move using `minimax()`  
4. Board updates  
5. Process repeats until:
   - someone wins, or
   - board is full  

---

## ▶️ How to Run

```bash
cd tic_tac_toe
python gui.py
```
---

## 📁 Project Structure
```bash
tic_tac_toe/
├── tictactoe.py     # Game logic + Minimax + Alpha-Beta Pruning
├── gui.py           # Tkinter GUI interface
└── README.md        # Project documentation
```

--- 

## 💡 Key Concepts
- Adversarial search
- Game trees
- Minimax algorithm
- Recursion
- State-space exploration
- Optimal decision-making
- Alpha-Beta Pruning

## 🚀 Possible Improvements
- Difficulty levels (depth-limited minimax)
- Better UI (colors, animations)
- AI vs AI mode
- Move explanation (why AI chose a move)

---

## 👩🏻‍💻 Author

Developed as part of learning Artificial Intelligence fundamentals, focusing on adversarial search and game theory.

