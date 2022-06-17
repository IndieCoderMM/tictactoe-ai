from tictactoe.board import Board
from tictactoe.gui import Gui
from tictactoe.engine import Engine

import pygame
import time

def main():
    board = Board()
    human = board.P1
    ai_player = board.P2 if human == board.P1 else board.P1

    ai = Engine(ai_player, human)
    gui = Gui(board, "Tic Tac Toe Pro")
    clock = pygame.time.Clock()

    running = True
    while running:
        if board.turn == ai.ai and not board.is_gameover():
            ai_move = ai.evaluate_best_move(board)
            board.push(ai_move)
            time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if board.is_gameover():
                    board.reset()
                    continue
                if board.turn != human:
                    continue
                tile = gui.get_clicked_tile(event.pos)
                board.push(tile)

        gui.update_display()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
