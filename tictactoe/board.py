from typing import Optional

Square = int
Symbol = str

class Board:
    P1 = 'O'
    P2 = 'X'
    EMPTY = '#'

    def __init__(self, size: int = 3):
        self.size = size
        self.p1_score = 0
        self.p2_score = 0

        self.SQUARES = self._squares()
        self.ROWS, self.COLS = self._rows_cols()
        self.DIAS = self._diagonals()
        self.WIN_CONDITIONS = self.ROWS + self.COLS + self.DIAS

        self.first_move = self.P1
        self.turn = self.P1
        self.table = self._new_table()

    def _squares(self) -> dict:
        """Dictionary containing square name
        for each row, column in table
        """
        return {(r, c): r*self.size+c for r in range(self.size) for c in range(self.size)}

    def _new_table(self) -> list[Symbol]:
        """Empty list for storing player's value
        """
        return [self.EMPTY for _ in range(self.size**2)]

    def _rows_cols(self) -> tuple[list, list]:
        """Return lists of rows and columns
        """
        rows: list[list] = [[] for _ in range(self.size)]
        columns: list[list] = [[] for _ in range(self.size)]
        for index, square in self.SQUARES.items():
            r, c = index
            rows[r].append(square)
            columns[c].append(square)
        return rows, columns

    def _diagonals(self) -> list:
        """Return lists of diagonals
        """
        diagonals: list[list] = [[], []]
        i = 0
        j = self.size-1
        for _ in range(self.size):
            diagonals[0].append(i)
            diagonals[1].append(j)
            i += self.size + 1
            j += self.size - 1
        return diagonals

    @property
    def empty_squares(self) -> list[Square]:
        """Return the list of indices of empty squares
        """
        return [square for square in self.SQUARES.values() if self.is_empty(square)]

    def reset(self) -> None:
        """Set the board to starting position
        for the next game
        """
        self.table = self._new_table()
        self.first_move = self.P2 if self.first_move == self.P1 else self.P1
        self.turn = self.first_move

    def square_pos(self, square: Square) -> Optional[tuple]:
        """Return the row, col according to
        the index of the square in board's table
        """
        for pos, sq in self.SQUARES.items():
            if sq == square:
                return pos
        return None

    def square_name(self, row: int, col: int) -> Square:
        """Return the index of the square in the
        board's table
        """
        return self.SQUARES[(row, col)]

    def square_value(self, square: Square) -> Symbol:
        """Return the value stored in square's index
        """
        return self.table[square]

    def is_empty(self, square: Square) -> bool:
        """Check if the square is occupied
        """
        return self.table[square] == self.EMPTY

    def get_connection(self) -> list[Square]:
        """Return the connected player if exists
        """
        for row in self.WIN_CONDITIONS:
            checklist = []
            for square in row:
                if self.is_empty(square):
                    continue
                checklist.append(self.square_value(square))
            if len(checklist) == self.size and len(set(checklist)) == 1:
                return row
        return []

    def is_draw(self) -> bool:
        """Check if the current position is draw
        """
        if len(self.empty_squares) == 0 and len(self.get_connection()) == 0:
            return True
        return False

    def winner(self) -> Optional[Symbol]:
        """Return the winner of the match if exists
        """
        connection = self.get_connection()
        if len(connection) == 0:
            return None
        elif self.square_value(connection[0]) == self.P1:
            return self.P1
        else:
            return self.P2

    def is_gameover(self) -> bool:
        """Check if the current game is terminated
        """
        return self.winner() is not None or self.is_draw()

    def _update(self) -> None:
        """Update the status of the game
        """
        self.turn = self.P2 if self.turn == self.P1 else self.P1
        if self.winner() == self.P1:
            self.p1_score += 1
        elif self.winner() == self.P2:
            self.p2_score += 1

    def push(self, square: Square, value: Symbol) -> None:
        """Store the given value in square index
        """
        self.table[square] = value

    def undo(self, square: Square) -> None:
        """Clear the value in square index
        """
        self.table[square] = self.EMPTY

    def move(self, square: Square) -> None:
        """Make the given move on the board if available
        """
        if square >= self.size**2 or square < 0 or not self.is_empty(square):
            print("Invalid move!")
            return
        self.push(square, self.turn)
        self._update()

    def print(self) -> None:
        """Display the current board
        in command line interface
        """
        if self.winner():
            print("Match Over!")
            print("*"*13)
        else:
            print("*" * 15)
            print("Turn->> ", self.turn)
            print('-' * (self.size*5))
        for index, square in self.SQUARES.items():
            r, c = index
            sign = square if self.is_empty(square) else self.square_value(square)
            print(' |', end=' ')
            print(sign, end='')
            if c == self.size-1:
                print(' |')
                print('-'*(self.size*5))
        print('-'*(self.size*5))
        print()


if __name__ == "__main__":
    # CLI game for two player mode
    board = Board()
    print("Tic Tac Toe - Duel")
    print("##################")
    board.print()
    running = True
    while running:
        move = int(input(f"Enter {board.turn} 's move: "))
        board.move(move)
        board.print()
        if board.is_gameover():
            running = False
    if board.is_draw():
        print("Draw! What a great match!")
    else:
        print(board.winner(), " Wins....!")
