from .board import Board
from .constants import MARGIN, WINDOW_WIDTH, P1_LOGO, P2_LOGO, P1_AVATAR, P2_AVATAR, WHITE, PURPLE, GREEN
from typing import Optional

import pygame

class Gui:
    def __init__(self, board: Board, title: str) -> None:
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
        pygame.display.set_caption(title)

        self.board = board
        self.boardwidth = WINDOW_WIDTH - MARGIN * 2
        self.tilewidth = self.boardwidth // self.board.size
        self.p1_logo = pygame.transform.scale(P1_LOGO, (self.tilewidth - 3, self.tilewidth - 3))
        self.p2_logo = pygame.transform.scale(P2_LOGO, (self.tilewidth - 3, self.tilewidth - 3))

    def draw_board(self) -> None:
        board_rect = (MARGIN-4, MARGIN-4, self.boardwidth+5, self.boardwidth+5)
        self.draw_square(board_rect, GREEN)

        for row in range(self.board.size):
            for col in range(self.board.size):
                rect = self.get_tile_rect(row, col)
                square = self.board.square_name(row, col)
                self.draw_square(rect, WHITE, self.board.square_value(square))

    def get_tile_rect(self, row: int, col: int) -> tuple:
        x_coor = MARGIN + self.tilewidth * col
        y_coor = MARGIN + self.tilewidth * row
        return x_coor, y_coor, self.tilewidth - 3, self.tilewidth - 3

    def draw_square(self, rect: tuple, color: tuple, value: str = None) -> None:
        pygame.draw.rect(self.window, color, rect)
        if value == self.board.P1:
            self.window.blit(self.p1_logo, rect)
        elif value == self.board.P2:
            self.window.blit(self.p2_logo, rect)

    def display_text(self, text: str, size: int, y: int, color: tuple = WHITE) -> None:
        font = pygame.font.Font('freesansbold.ttf', size)
        text_box = font.render(text, True, color)
        x = WINDOW_WIDTH//2 - text_box.get_width()//2
        self.window.blit(text_box, (x, y))

    def display_status(self) -> None:
        self.window.blit(P1_AVATAR, (10, 10))
        self.window.blit(P2_AVATAR, (WINDOW_WIDTH-60, 10))

        if self.board.is_draw():
            self.display_text("Draw!", 50, 20)
        elif self.board.winner() == self.board.P1:
            self.display_text("Newbie Wins!", 50, 20)
        elif self.board.winner() == self.board.P2:
            self.display_text("Batman Wins!", 50, 20)
        else:
            if self.board.turn == self.board.P1:
                self.display_text("Newbie is thinking...", 20, WINDOW_WIDTH-50)
            else:
                self.display_text("Batman is thinking...", 20, WINDOW_WIDTH-50)

    def update_display(self) -> None:
        self.window.fill(PURPLE)
        self.draw_board()
        self.display_status()
        pygame.display.update()

    def get_clicked_tile(self, coor: tuple) -> Optional[int]:
        x, y = coor
        for row in range(self.board.size):
            for col in range(self.board.size):
                rect = pygame.Rect(self.get_tile_rect(row, col))
                if rect.collidepoint(x, y):
                    return self.board.SQUARES[(row, col)]
        return None
