from .board import Board
from typing import Optional

import pygame

STARIMG = pygame.image.load("assets/star.png")
CROSSIMG = pygame.image.load("assets/error.png")
AVATAR1 = pygame.transform.scale(pygame.image.load("assets/happy.png"), (50, 50))
AVATAR2 = pygame.transform.scale(pygame.image.load("assets/batman.png"), (50, 50))

MARGIN = 100
GREEN = (39, 174, 96)
GREY = (44, 62, 80)
PURPLE = (142, 68, 173)
WHITE = (255, 255, 255)

class Gui:
    def __init__(self, width: int, height: int, board: Board, title: str) -> None:
        self.width = width
        self.height = height
        self.board = board
        self.tilesize = (self.width - MARGIN * 2) // self.board.size
        self.circle_img = pygame.transform.scale(STARIMG, (self.tilesize - 5, self.tilesize - 5))
        self.cross_img = pygame.transform.scale(CROSSIMG, (self.tilesize - 5, self.tilesize - 5))

        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

    def draw_board(self) -> None:
        for row in range(self.board.size):
            for col in range(self.board.size):
                rect = self.get_tile_rect(row, col)
                square_name = self.board.SQUARES[(row, col)]
                self.draw_square(rect, self.board.table[square_name])

    def get_tile_rect(self, row: int, col: int) -> tuple:
        x_coor = MARGIN + self.tilesize * col
        y_coor = MARGIN + self.tilesize * row
        return x_coor, y_coor, self.tilesize-3, self.tilesize-3

    def draw_square(self, rect: tuple, val: str) -> None:
        pygame.draw.rect(self.window, WHITE, rect)
        if val == self.board.P1:
            self.window.blit(self.circle_img, rect)
        elif val == self.board.P2:
            self.window.blit(self.cross_img, rect)

    def display_text(self, text: str, size: int, y: int, color: tuple = WHITE) -> None:
        font = pygame.font.Font('freesansbold.ttf', size)
        text_box = font.render(text, True, color)
        x = self.width//2 - text_box.get_width()//2
        self.window.blit(text_box, (x, y))

    def display_status(self) -> None:
        self.window.blit(AVATAR1, (10, 10))
        self.window.blit(AVATAR2, (self.width-60, 10))

        if self.board.is_draw():
            self.display_text("Draw!", 50, 20)
        elif self.board.winner() == self.board.P1:
            self.display_text("Newbie Wins!", 50, 20)
        elif self.board.winner() == self.board.P2:
            self.display_text("Batman Wins!", 50, 20)
        else:
            if self.board.turn == self.board.P1:
                self.display_text("Newbie is thinking...", 20, self.height-50)
            else:
                self.display_text("Batman is thinking...", 20, self.height-50)

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
