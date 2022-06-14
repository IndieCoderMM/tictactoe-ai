from tictactoe.board import Board
from tictactoe.gui import Gui
from minimax.engine import Engine

import pygame
import time

def main():
    board = Board()
    gui = Gui(500, 500, board, "Tic Tac Toe Pro")
    player = board.P1
    ai = board.P2
    engine = Engine(ai, player)
    clock = pygame.time.Clock()

    running = True
    while running:
        if board.turn == ai and not board.is_gameover():
            ai_move = engine.evaluate_best_move(board)
            board.push(ai_move)
            time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if board.is_gameover():
                    board.reset()
                    continue
                if board.turn != player:
                    continue
                tile = gui.get_clicked_tile(event.pos)
                board.push(tile)

        gui.update_display()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
