import pygame
import time

from tictactoe.board import Board, Symbol
from tictactoe.gui import Gui
from tictactoe.engine import Engine

MODE = "TERMINATOR"
# MODE = "2 Player"


def main():
    board = Board()
    p1 = Symbol.CIRCLE
    p2 = Symbol.CROSS if p1 == Symbol.CIRCLE else Symbol.CIRCLE

    ai = Engine(p2, p1, 9)
    gui = Gui(board, "Tic Tac Toe Pro", MODE)
    clock = pygame.time.Clock()

    running = True
    while running:
        gui.update_display()
        clock.tick(30)

        if MODE == "TERMINATOR":
            if board.turn == ai.ai and not board.is_gameover():
                ai_move = ai.evaluate_best_move(board)
                board.move(ai_move)
                time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if board.is_gameover():
                    board.reset()
                    continue
                tile = gui.get_clicked_tile(event.pos)
                if tile is not None:
                    board.move(tile)

    pygame.quit()


if __name__ == "__main__":
    main()
