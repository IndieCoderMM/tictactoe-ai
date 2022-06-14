from tictactoe.board import Board

class Engine:
    def __init__(self, ai: str, player: str) -> None:
        self.ai = ai
        self.player = player

    def minimax(self, board: Board, ai_turn: bool, last_move: int) -> tuple:
        available_moves = board.empty_squares()
        if len(available_moves) == 0 or board.is_gameover():
            return self.evaluate_board(board), last_move

        if ai_turn:
            max_eval = -1000
            best_move = None
            for move in available_moves:
                board.move(move, self.ai)
                eval_ = self.minimax(board, False, move)[0]
                board.undo(move)
                max_eval = max(max_eval, eval_)
                if max_eval == eval_:
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = 1000
            best_move = None
            for move in available_moves:
                board.move(move, self.player)
                eval_ = self.minimax(board, True, move)[0]
                board.undo(move)
                min_eval = min(min_eval, eval_)
                if min_eval == eval_:
                    best_move = move
            return min_eval, best_move

    def evaluate_board(self, board: Board) -> int:
        if board.winner() == self.ai:
            return 1
        elif board.winner() == self.player:
            return -1
        return 0

    def evaluate_best_move(self, board: Board) -> int:
        _, best_move = self.minimax(board, True, 0)
        return best_move

