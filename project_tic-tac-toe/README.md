# Tic-Tac-Toe (Python CLI)

A command-line Tic-Tac-Toe game written in Python where you (`O`) play against the computer (`X`). Built using only the Python standard library.

## How the Game Works

- The board is a `3x3` grid numbered `1` through `9`.
- The computer (`X`) makes the opening move in the center square (`5`).
- You (`O`) enter a number from `1` to `9` to place your mark on an open square.
- The game validates every input against invalid characters, out-of-range numbers, and occupied squares.
- Play continues until either side aligns three marks (horizontally, vertically, or diagonally) or all squares are filled for a tie.

## Sample Output

```text
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
```

## Getting Started

### Prerequisites

- Python 3.x (no external packages required)

### Run Locally

```bash
git clone [https://github.com/kedaragisetti/mylearningak_python.git](https://github.com/kedaragisetti/mylearningak_python.git)
cd mylearningak_python/project_tic-tac-toe
python tic_tac_toe.py
```

## Key Concepts Demonstrated

- **2D Lists & Grid Indexing:** Representing the `3x3` board as nested lists and mapping board numbers `1–9` to `(row, col)` indices using `// 3` and `% 3`.
- **Tuples & List Comprehensions / Iteration:** Tracking available moves dynamically as `(row, col)` coordinate tuples.
- **Modular Function Design:** Separating board rendering, input validation, AI move selection (`random.randrange`), and win-condition checks into dedicated functions.
- **Defensive Input Validation:** Guarding against non-numeric inputs, out-of-bounds values, and duplicate moves inside a `while` loop.