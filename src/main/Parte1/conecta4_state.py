# src/main/Parte1/conecta4_state.py
from copy import deepcopy
from typing import List, Optional
from stategame import StateGame

ROWS = 6
COLS = 7

class Conecta4State(StateGame):
    """
    Conecta-4 (4 en raya) state implementation.
    Board is a list of lists: board[row][col], row 0 top, row 5 bottom.
    Players: 'X' (MAX) and 'O' (MIN). Empty cell: '.'
    """

    def __init__(self, board: Optional[List[List[str]]] = None, turn: str = 'X'):
        if board is None:
            self.board = [['.' for _ in range(COLS)] for _ in range(ROWS)]
        else:
            self.board = board
        self.turn = turn

    @classmethod
    def start(cls):
        return cls()

    def toMove(self) -> str:
        return self.turn

    def rival(self, player: str) -> str:
        return 'O' if player == 'X' else 'X'

    def clone_and_apply(self, col: int) -> "Conecta4State":
        """Return a new state with a disc dropped in column `col` for current turn."""
        new_board = deepcopy(self.board)
        # find lowest empty row in column
        for r in range(ROWS-1, -1, -1):
            if new_board[r][col] == '.':
                new_board[r][col] = self.turn
                break
        next_turn = self.rival(self.turn)
        return Conecta4State(new_board, next_turn)

    def legal_moves(self) -> List[int]:
        """Return list of column indices that are not full."""
        moves = []
        for c in range(COLS):
            if self.board[0][c] == '.':
                moves.append(c)
        return moves

    def actionResults(self) -> List["Conecta4State"]:
        moves = self.legal_moves()
        children = [self.clone_and_apply(c) for c in moves]
        return children

    def is_full(self) -> bool:
        return all(self.board[0][c] != '.' for c in range(COLS))

    def isTerminal(self) -> bool:
        return self._check_win('X') or self._check_win('O') or self.is_full()

    def _check_win(self, player: str) -> bool:
        b = self.board
        # horizontal
        for r in range(ROWS):
            for c in range(COLS - 3):
                if all(b[r][c+i] == player for i in range(4)):
                    return True
        # vertical
        for c in range(COLS):
            for r in range(ROWS - 3):
                if all(b[r+i][c] == player for i in range(4)):
                    return True
        # diag down-right
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                if all(b[r+i][c+i] == player for i in range(4)):
                    return True
        # diag up-right
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                if all(b[r-i][c+i] == player for i in range(4)):
                    return True
        return False

    def winner(self) -> Optional[str]:
        if self._check_win('X'):
            return 'X'
        if self._check_win('O'):
            return 'O'
        return None

    # ---------- Heuristic evaluation ----------
    def heuristicUtility(self, player: str) -> int:
        """Heuristic: counts windows of length 4 and values patterns:
           4 in a row (win) -> huge
           3 in a row open -> +100
           2 in a row open -> +10
           subtract same for opponent.
        """
        opponent = self.rival(player)

        if self._check_win(player):
            return 10_000_000
        if self._check_win(opponent):
            return -10_000_000

        score = 0
        score += self._score_position(player)
        score -= self._score_position(opponent)
        return score

    def _score_position(self, player: str) -> int:
        b = self.board
        score = 0

        def window_score(window: List[str]):
            p_count = window.count(player)
            empty_count = window.count('.')
            if p_count == 4:
                return 10000
            elif p_count == 3 and empty_count == 1:
                return 100
            elif p_count == 2 and empty_count == 2:
                return 10
            return 0

        # horizontal windows
        for r in range(ROWS):
            for c in range(COLS - 3):
                w = [b[r][c+i] for i in range(4)]
                score += window_score(w)

        # vertical windows
        for c in range(COLS):
            for r in range(ROWS - 3):
                w = [b[r+i][c] for i in range(4)]
                score += window_score(w)

        # diag down-right
        for r in range(ROWS - 3):
            for c in range(COLS - 3):
                w = [b[r+i][c+i] for i in range(4)]
                score += window_score(w)

        # diag up-right
        for r in range(3, ROWS):
            for c in range(COLS - 3):
                w = [b[r-i][c+i] for i in range(4)]
                score += window_score(w)

        return score

    def toString(self) -> str:
        lines = []
        for r in range(ROWS):
            lines.append(' '.join(self.board[r]))
        return '\n'.join(lines)

    def pretty_print(self):
        print(self.toString())
        print('0 1 2 3 4 5 6')  # column indices

    # utility to perform move by column index in-place (used for interactive)
    def apply_move_inplace(self, col: int):
        for r in range(ROWS-1, -1, -1):
            if self.board[r][col] == '.':
                self.board[r][col] = self.turn
                self.turn = self.rival(self.turn)
                return
        raise ValueError(f"Column {col} is full")
