![LastUpdate](https://img.shields.io/github/last-commit/IndieCoderMM/tictactoe-ai)
[![Forks](https://img.shields.io/github/forks/IndieCoderMM/tictactoe-ai)](https://github.com/IndieCoderMM/tictactoe-ai/network/members)
![Stars](https://img.shields.io/github/stars/IndieCoderMM/tictactoe-ai)
[![License](https://img.shields.io/github/license/IndieCoderMM/tictactoe-ai.svg)](https://github.com/IndieCoderMM/tictactoe-ai/blob/master/LICENSE)

## Table of Contents

- [🤖 Tic-Tac-Toe Terminator](#-tic-tac-toe-terminator)
  - [🛠 Technology](#-technology)
  - [📸 Screenshots](#-screenshots)
  - [💾 Installation](#-installation)
  - [🎮 Tictactoe](#-tictactoe)
  - [🤝 Contributing](#-contributing)
  - [📜 License](#-license)
  - [💖 Show your support](#-show-your-support)

# 🤖 Tic-Tac-Toe Terminator

**Tic-Tac-Toe Terminator** is a computer player that uses the minimax algorithm to make its moves. This algorithm allows the A.I. to analyze the current state of the game and determine the best move to make in order to maximize its chances of winning.

The A.I. is designed to be unbeatable, meaning it will always either win or draw against a human opponent. To achieve this level of performance, the A.I. prunes unnecessary branches of the game tree to make its calculations more efficient.

## 🛠 Technology

- Python
- Pygame library
- Minimax algorithm

## 📸 Screenshots

<img src="./tictactoe_demo.gif" width="500" title="vs AI mode">

## 💾 Installation

1. Clone this repo

```sh
git clone git@github.com:IndieCoderMM/tictactoe-ai.git
```

2. Install pygame library

```sh
pip install pygame
```

3. Run the program

```sh
python main.py
```

## 🎮 Tictactoe

**Tictactoe** game can also be played without engine.

- Inside **tictactoe** package, there are 3 modules:
  1. `board.py`: Game logics
  2. `gui.py`: Pygame interface
  3. `engine.py`: Algorithm
- You can play the 2 player mode in the console, by running the `python tictactoe/board.py`.
- You can also change the board size (4x4, 5x5, etc.). (_A.I. can only play 3x3 board currently_)
- By changing `MODE` in `main.py`, you can play the 2P version in pygame interface.

<img src="./tictactoe_2p_demo.gif" width="300" title="2 Player Mode">

## 🤝 Contributing

I welcome any and all contribution that can help me improve my project. If you have any ideas or feedback that you'd like to share, please don't hesitate to reach out.

## 📜 License

This project is licensed under the [MIT](./LICENSE) license.

## 💖 Show your support

If you found this project interesting or helpful, please consider giving it a ⭐.
