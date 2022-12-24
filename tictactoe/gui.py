import pygame
from .board import Board, Symbol

WINDOW_WIDTH = 500
MARGIN = 100
PROFILE_SIZE = WINDOW_WIDTH // 10

P1_LOGO = pygame.image.load("assets/star.png")
P2_LOGO = pygame.image.load("assets/error.png")
P1_IMG = pygame.image.load("assets/happy.png")
P2_IMG = pygame.image.load("assets/batman.png")

P1_AVATAR = pygame.transform.scale(P1_IMG, (PROFILE_SIZE, PROFILE_SIZE))
P1_RECT = pygame.Rect(10, 10, PROFILE_SIZE, PROFILE_SIZE)
P2_AVATAR = pygame.transform.scale(P2_IMG, (PROFILE_SIZE, PROFILE_SIZE))
P2_RECT = pygame.Rect(WINDOW_WIDTH - P2_AVATAR.get_width() - 10, 10,
                      PROFILE_SIZE, PROFILE_SIZE)

GREEN = (118, 255, 3)
BLUE = (41, 128, 185)
RED = (189, 8, 28)
GREY = (52, 73, 94)
WHITE = (236, 240, 241)
YELLOW = (241, 196, 15)


class Gui:

    def __init__(self, board: Board, title: str, mode) -> None:
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
        pygame.display.set_caption(
            f'{title} ({"vs Terminator" if mode == "TERMINATOR" else "2 Player"})'
        )
        self.board = board
        self._set_up()

    def _set_up(self):
        self.boardwidth = WINDOW_WIDTH - MARGIN * 2
        self.tilewidth = self.boardwidth // self.board.size
        self.p1_logo = pygame.transform.scale(
            P1_LOGO, (self.tilewidth - 3, self.tilewidth - 3))
        self.p2_logo = pygame.transform.scale(
            P2_LOGO, (self.tilewidth - 3, self.tilewidth - 3))

    def get_tile_rect(self, row, col, margin=0):
        x_coor = MARGIN + self.tilewidth * col
        y_coor = MARGIN + self.tilewidth * row
        return x_coor, y_coor, self.tilewidth - margin, self.tilewidth - margin

    def get_clicked_tile(self, coor):
        x, y = coor
        for row in range(self.board.size):
            for col in range(self.board.size):
                rect = pygame.Rect(self.get_tile_rect(row, col, 3))
                if rect.collidepoint(x, y):
                    return self.board.squares[(row, col)]

    def draw_square(self, rect, color, value=None):
        pygame.draw.rect(self.window, color, rect)
        if value == Symbol.CIRCLE:
            self.window.blit(self.p1_logo, rect)
        elif value == Symbol.CROSS:
            self.window.blit(self.p2_logo, rect)

    def draw_board(self):
        board_rect = (MARGIN - 4, MARGIN - 4, self.boardwidth + 5,
                      self.boardwidth + 5)
        self.draw_square(board_rect, GREY)
        connection = self.board.get_connection()
        for row in range(self.board.size):
            for col in range(self.board.size):
                color = YELLOW if self.board.square_name(
                    row, col) in connection else WHITE
                rect = self.get_tile_rect(row, col, 3)
                square = self.board.square_name(row, col)
                self.draw_square(rect, color, self.board.square_value(square))

    def display_text(self, text, size, x, y, color=WHITE):
        font = pygame.font.Font('freesansbold.ttf', size)
        text_box = font.render(text, True, color)
        if x == 'center':
            x = WINDOW_WIDTH // 2 - text_box.get_width() // 2
        self.window.blit(text_box, (x, y))

    def display_status(self):
        pygame.draw.circle(self.window, RED, P1_RECT.center,
                           PROFILE_SIZE // 2 + 3)
        pygame.draw.circle(self.window, RED, P2_RECT.center,
                           PROFILE_SIZE // 2 + 3)
        if self.board.is_draw():
            self.display_text("Draw!", 50, 'center', WINDOW_WIDTH - 50)
        elif self.board.winner() == Symbol.CIRCLE:
            self.display_text("Newbie Wins!", 50, 'center',
                              WINDOW_WIDTH - MARGIN + 10)
        elif self.board.winner() == Symbol.CROSS:
            self.display_text("Batman Wins!", 50, 'center',
                              WINDOW_WIDTH - MARGIN + 10)
        else:
            if self.board.turn == Symbol.CIRCLE:
                self.display_text("Newbie is thinking...", 20, 'center',
                                  WINDOW_WIDTH - MARGIN + 10)
                pygame.draw.circle(self.window, GREEN, P1_RECT.center,
                                   PROFILE_SIZE // 2 + 5, 3)
            else:
                self.display_text("Batman is thinking...", 20, 'center',
                                  WINDOW_WIDTH - MARGIN + 10)
                pygame.draw.circle(self.window, GREEN, P2_RECT.center,
                                   PROFILE_SIZE // 2 + 5, 3)

        self.window.blit(P1_AVATAR, P1_RECT)
        self.window.blit(P2_AVATAR, P2_RECT)
        self.display_text(f'{str(self.board.p1_score)}', 50, PROFILE_SIZE + 20,
                          20, YELLOW)
        self.display_text(f'{str(self.board.p2_score)}', 50,
                          WINDOW_WIDTH - PROFILE_SIZE - 50, 20, YELLOW)

    def update_display(self):
        self.window.fill(BLUE)
        self.draw_board()
        self.display_status()
        pygame.display.update()
