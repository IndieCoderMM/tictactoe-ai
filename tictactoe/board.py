from typing import Optional

class Board:
    P1 = 'O'
    P2 = 'X'
    EMPTY = ' '

    def __init__(self, size: int = 3) -> None:
        self.size = size
        self.first_move = None
        self.turn = None
        self.table = None

        self.SQUARES = self._squares()
        self.ROWS, self.COLS = self._rows_cols()
        self.DIAS = self._diagonals()
        self.WIN_CONDITIONS = self.ROWS + self.COLS + self.DIAS

        self.reset()

    def _squares(self) -> dict:
        """Dictionary containing square name
        for each row, column in table
        """
        return {(r, c): r*self.size+c for r in range(self.size) for c in range(self.size)}

    def _new_table(self) -> list:
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
        i = 1
        j = self.size
        for _ in range(self.size):
            diagonals[0].append(i)
            diagonals[1].append(j)
            i += self.size + 1
            j += self.size - 1
        return diagonals

    def reset(self) -> None:
        """Set the board to starting position
        for the next game
        """
        self.table = self._new_table()
        self.first_move = self.P2 if self.first_move == self.P1 else self.P1
        self.turn = self.first_move

    def print(self) -> None:
        """Display the current board
        in command line interface
        """
        if self.winner():
            print("Match Over!")
            print("*"*13)
        else:
            print("Turn->> ", self.turn)
            print('-' * (self.size*5))
        for index, square in self.SQUARES.items():
            r, c = index
            sign = square if self.is_empty(square) else self.square_value(square)
            print(' |', end=' ')
            print(sign, end='')
            if c == self.size-1:
                print('|')
                print('-'*(self.size*5))
        print('#'*(self.size*5))

    def square_pos(self, square: int) -> Optional[tuple]:
        """Return the row, col according to
        the index of the square in board's table
        """
        for index, sq in self.SQUARES.items():
            if sq == square:
                return index
        return None

    def square_name(self, row: int, col: int) -> int:
        """Return the index of the square in the
        board's table
        """
        return self.SQUARES[(row, col)]

    def square_value(self, square: int) -> str:
        """Return the value stored in square's index
        """
        return self.table[square]

    def is_empty(self, square: int) -> bool:
        """Check if the square is occupied
        """
        return self.table[square] == self.EMPTY

    def empty_squares(self) -> list[int]:
        """Return the list of indices of empty squares
        """
        return [square for square in self.SQUARES.values() if self.is_empty(square)]

    def move(self, square: int, value: str) -> bool:
        """Store the given value in square index
        if available
        """
        if not self.is_empty(square):
            return False
        self.table[square] = value
        return True

    def undo(self, square: int) -> None:
        """Clear the value in square index
        """
        self.table[square] = self.EMPTY

    def push(self, square: Optional[int]) -> None:
        """Store the given move on the board and
        change the turn
        """
        if square is None or not self.move(square, self.turn):
            return
        self.turn = self.P2 if self.turn == self.P1 else self.P1

    def is_draw(self) -> bool:
        """Check if the current position is draw
        """
        if self.check_connection() is None and len(self.empty_squares()) == 0:
            return True
        return False

    def is_gameover(self) -> bool:
        """Check if the current game is terminated
        """
        return self.winner() is not None or self.is_draw()

    def winner(self) -> Optional[str]:
        """Return the winner of the match if exists
        """
        connected = self.check_connection()
        if connected == self.P1:
            return self.P1
        elif connected == self.P2:
            return self.P2
        return None

    def check_connection(self) -> Optional[str]:
        """Return the connected player if exists
        """
        for row in self.WIN_CONDITIONS:
            checklist = []
            for square in row:
                if self.is_empty(square):
                    continue
                checklist.append(self.square_value(square))
            if len(checklist) == self.size and len(set(checklist)) == 1:
                return checklist[0]
        return None


if __name__ == "__main__":
    # CLI game for two player mode
    board = Board(3)
    board.print()
    running = True
    while running:
        move = int(input(f"Enter {board.turn} 's move: "))
        board.push(move)
        board.print()
        if board.is_gameover():
            running = False
    if board.is_draw():
        print("Draw! What a great match!")
    else:
        print(board.winner(), " Wins....!")
