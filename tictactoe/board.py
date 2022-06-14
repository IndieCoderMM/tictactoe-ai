from typing import Optional

class Board:
    P1 = 'O'
    P2 = 'X'
    EMPTY = ' '
    DRAW = 11

    def __init__(self, size: int = 3) -> None:
        self.size = size
        self.first_move = self.P1
        self.turn = self.first_move

        self.SQUARES = self._squares()
        self.ROWS, self.COLS = self._get_rows_cols()
        self.DIAS = self._get_diagonals()
        self.WIN_CONDITIONS = self.ROWS + self.COLS + self.DIAS
        self.table = self._new_table()

    def _squares(self) -> dict:
        return {(r, c): r*self.size+c+1 for r in range(self.size) for c in range(self.size)}

    def _get_rows_cols(self) -> tuple[list, list]:
        rows: list[list] = [[] for _ in range(self.size)]
        columns: list[list] = [[] for _ in range(self.size)]
        for index, square in self.SQUARES.items():
            r, c = index
            rows[r].append(square)
            columns[c].append(square)
        return rows, columns

    def _get_diagonals(self) -> list:
        diagonals: list[list] = [[], []]
        i = 1
        j = self.size
        for _ in range(self.size):
            diagonals[0].append(i)
            diagonals[1].append(j)
            i += self.size + 1
            j += self.size - 1
        return diagonals

    def _new_table(self) -> dict:
        return {square: self.EMPTY for square in self.SQUARES.values()}

    def reset(self) -> None:
        self.table = self._new_table()
        self.first_move = self.P2 if self.first_move == self.P1 else self.P1
        self.turn = self.first_move

    def print(self) -> None:
        if self.winner():
            print("Match Over!")
            print("*"*13)
        else:
            print("Turn->> ", self.turn)
            print('-' * 13)
        for index, square_name in self.SQUARES.items():
            r, c = index
            sign = square_name if self.is_empty(square_name) else self.table[square_name]
            print('|', end=' ')
            print(sign, end=' ')
            if c == self.size-1:
                print('|')
                print('-'*13)

    def get_tile_index(self, square: int) -> Optional[tuple]:
        for k, v in self.SQUARES.items():
            if v == square:
                return k
        return None

    def is_empty(self, square: int) -> bool:
        return self.table[square] == self.EMPTY

    def empty_squares(self) -> list[int]:
        return [square for square in self.SQUARES.values() if self.is_empty(square)]

    def move(self, square: int, symbol: str) -> bool:
        if not self.is_empty(square):
            return False
        self.table[square] = symbol
        return True

    def undo(self, square: int) -> None:
        self.table[square] = self.EMPTY

    def push(self, square: Optional[int]) -> None:
        if square is None:
            return
        if not self.move(square, self.turn):
            print("Invalid Move!")
            return
        self.turn = self.P2 if self.turn == self.P1 else self.P1

    def is_draw(self) -> bool:
        if self.check_connection() is None and len(self.empty_squares()) == 0:
            return True
        return False

    def winner(self) -> Optional[str]:
        connected = self.check_connection()
        if connected == self.P1:
            return self.P1
        elif connected == self.P2:
            return self.P2
        return None

    def is_gameover(self) -> bool:
        return self.winner() is not None or self.is_draw()

    def check_connection(self) -> Optional[str]:
        for row in self.WIN_CONDITIONS:
            checklist = []
            for square_name in row:
                if self.is_empty(square_name):
                    continue
                checklist.append(self.table[square_name])
            if len(checklist) == self.size and len(set(checklist)) == 1:
                return checklist[0]
        return None

def main():
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


if __name__ == "__main__":
    main()
