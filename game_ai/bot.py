
from core.types import PieceType
from core.board import Board
from .utils import find_random_move, find_best_move

def random_bot_move(board: Board):
    bot_move = find_random_move(board)
    if bot_move is None:
        return None
    start, end = bot_move 
    promo = PieceType.QUEEN  # Bot default promotion to Queen if needed
    return (start, end, promo)

def minimax_bot_move(board: Board):
        if board.game_over:
            return

        board.switch_to_bot_mode(True)  # Ensure AI boards are bot board
        # Find best move using Minimax with Alpha-Beta Pruning
        bot_move = find_best_move(board)
        board.switch_to_bot_mode(False)  # Switch back to main board

        if bot_move is None:
            return
        start, end = bot_move 
        promo = PieceType.QUEEN  # Bot default promotion to Queen if needed
        return (start, end, promo)