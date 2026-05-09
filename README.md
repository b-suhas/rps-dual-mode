# Rock Paper Scissors – Dual Mode CLI Game

A clean, beginner-friendly **Rock Paper Scissors** game built in Python that runs entirely in the terminal. Supports both **Player vs Computer** and **Player vs Player** modes with a replay option after each round.

---

## Description

This is a command-line implementation of the classic Rock Paper Scissors game. It was built as a Python learning project to practise core programming concepts such as conditionals, loops, user input handling, and the `random` module.

Whether you want to challenge the computer or go head-to-head with a friend in the same terminal, this game has you covered.

---

## Features

-  **Player vs Computer** — the computer picks randomly using Python's `random` module
-  **Player vs Player** — two players take turns entering their choices in the same terminal
-  **Replay option** — choose to play again after every round
-  **Integer-based input** — Rock = `0`, Paper = `1`, Scissors = `2` for fast, clean input
-  **Pure Python** — no external libraries required

---

##  How the Game Works

Rock Paper Scissors is a two-player hand-gesture game governed by three rules:

| Gesture    | Beats    |
|------------|----------|
| 👊 Rock    | Scissors |
| ✂️ Scissors | Paper    |
| 📄 Paper   | Rock     |

- The player who defeats the other's gesture wins the round.
- If both players choose the same gesture, the round is a **draw**.

In this implementation, gestures are entered as numbers:
- `0` → Rock
- `1` → Paper
- `2` → Scissors

---

##  Installation

**Prerequisites:** Python 3.x must be installed. [Download Python here](https://www.python.org/downloads/).

```bash
# 1. Clone the repository
git clone https://github.com/b-suhas/rps-dual-mode

# 2. Navigate into the project folder
cd rps-dual-mode
```

No additional packages need to be installed — this project uses only the Python standard library.

---

## How to Run

```bash
python main.py
```

---

## Example Gameplay

**Player vs Computer**
```
Select mode:
1. Player vs Computer
2. Player vs Player
Enter choice: 1

Enter your choice — Rock(0), Paper(1), Scissors(2): 0
Computer chose: 2 (Scissors)

🎉 You win! Rock beats Scissors.

Play again? (yes/no): no
Thanks for playing!
```

**Player vs Player**
```
Select mode:
1. Player vs Computer
2. Player vs Player
Enter choice: 2

Player 1 — Enter your choice — Rock(0), Paper(1), Scissors(2): 1
Player 2 — Enter your choice — Rock(0), Paper(1), Scissors(2): 0

Player 1 wins! Paper beats Rock.

Play again? (yes/no): no
Thanks for playing!
```

---

## Project Structure

```
rps-dual-mode/
│
├── main.py        # Main game logic
└── README.md      # Project documentation
```

---

## Requirements

| Requirement | Details             |
|-------------|---------------------|
| Language    | Python 3.x          |
| Libraries   | `random` (built-in) |
| Platform    | Windows / macOS / Linux |

---

## Future Improvements

- [ ] **Score tracker** — keep a running tally across multiple rounds
- [ ] **Input validation** — handle invalid entries gracefully without crashing
- [ ] **Best-of-N mode** — play a best-of-3 or best-of-5 series
- [ ] **Gesture detection** — use a webcam and OpenCV/MediaPipe to detect real hand gestures
- [ ] **GUI version** — build a simple graphical interface using Tkinter or Pygame

---

## 👤 Author

**Your Name**
- GitHub: [@b-suhas](https://github.com/b-suhas)
- LinkedIn: [B SUHAS](https://www.linkedin.com/in/bsuhas/)

---

*Feel free to fork this project, open issues, or submit pull requests. Contributions are welcome!*
