from tictactoe.board import Board
import random

Square = int
Score = int


class Engine:

    def __init__(self, ai: str, foe: str, level: int):
        self.ai = ai
        self.foe = foe
        self.level = level

    def minimax(self, board: Board, ai_turn: bool, depth: int, alpha: float,
                beta: float) -> tuple:
        available_moves = board.empty_squares
        if len(available_moves) == board.size**2:
            return 0, random.choice(list(range(board.size**2)))
        if board.is_gameover() or depth >= self.level:
            return self.evaluate_board(board, depth), None

        if ai_turn:
            max_eval = float('-inf')
            best_move = None
            for move in available_moves:
                board.push(move, self.ai)
                eval_ = self.minimax(board, False, depth + 1, alpha, beta)[0]
                board.undo(move)
                max_eval = max(max_eval, eval_)
                if max_eval == eval_:
                    best_move = move
                alpha = max(alpha, max_eval)
                if alpha > beta:
                    return max_eval, best_move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in available_moves:
                board.push(move, self.foe)
                eval_ = self.minimax(board, True, depth + 1, alpha, beta)[0]
                board.undo(move)
                min_eval = min(min_eval, eval_)
                if min_eval == eval_:
                    best_move = move
                beta = min(min_eval, beta)
                if beta < alpha:
                    return min_eval, best_move
            return min_eval, best_move

    def evaluate_board(self, board: Board, depth: int) -> Score:
        if board.winner() == self.ai:
            return board.size**2 - depth
        elif board.winner() == self.foe:
            return -1 * board.size**2 - depth
        return 0

    def evaluate_best_move(self, board: Board) -> Square:
        best_move = self.minimax(board, True, 0, float('-inf'),
                                 float('inf'))[1]
        return best_move
