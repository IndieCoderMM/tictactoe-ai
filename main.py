import pygame
import time

from tictactoe.board import Board
from tictactoe.gui import Gui
from tictactoe.engine import Engine

def main():
    board = Board()
    human = board.P1
    ai_player = board.P2 if human == board.P1 else board.P1

    ai = Engine(ai_player, human, 9)
    gui = Gui(board, "Tic Tac Toe Pro")
    clock = pygame.time.Clock()

    running = True
    while running:
        gui.update_display()
        clock.tick(30)

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
                if board.turn != human:
                    continue
                tile = gui.get_clicked_tile(event.pos)
                if tile is not None:
                    board.move(tile)

    pygame.quit()


if __name__ == "__main__":
    main()
