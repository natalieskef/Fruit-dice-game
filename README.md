# Multiplayer Fruit Dice Challenge

A fun and interactive 2-player terminal-based dice game built with Python. Players compete over 3 structural rounds, rolling a standard 6-sided die alongside a randomized fruit selection that triggers special point combos.

## Features
* **Multiplayer System:** Supports custom player names via terminal inputs.
* **Randomized Gameplay:** Employs Python's `random` module (`randint` and `choice`) to ensure unique outcomes for every roll and fruit match.
* **Dynamic Scoring & Combos:** 
  * 🍒 **Cherry Combo:** Rolling a **6** with a **Cherry** grants a mega **+10 bonus points**.
  * 🍌 **Banana Bonus:** Getting a **Banana** rewards **+6 bonus points** regardless of the dice value.
* **Round-by-Round Breakdown:** Displays intermediate scores and combinations for each round, leading up to a final scoreboard.

## Tech Stack & Concepts Covered
* **Language:** Python 3
* **Libraries:** `random` (Standard Library)
* **Core Concepts:** Functions, Loops (`for` with `range`), Conditional Logic (`if-elif-else`), and String Interpolation (f-strings).

## How to Run
1. Clone this repository.
2. Run the script using Python:
   ```bash
   python main.py
