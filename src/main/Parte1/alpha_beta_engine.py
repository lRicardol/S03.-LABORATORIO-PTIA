# src/main/Parte1/alpha_beta_engine.py
from typing import Tuple
from conecta4_state import Conecta4State

class AlphaBetaEngine:
    """
    MiniMax with alpha-beta pruning engine for StateGame-like objects.
    """

    @staticmethod
    def search(state: Conecta4State, depth: int) -> Tuple[int, Conecta4State]:
        """
        Returns a tuple (best_move_column, best_child_state).
        best_move_column is the column index chosen (int) or -1 if no move.
        """
        player = state.toMove()
        best_col = -1
        best_state = None

        if player == 'X':
            best_val = -float('inf')
            alpha = -float('inf')
            beta = float('inf')
            for col in state.legal_moves():
                child = state.clone_and_apply(col)
                val = AlphaBetaEngine.minValue(child, depth-1, alpha, beta, 'X')
                if val > best_val:
                    best_val = val
                    best_col = col
                    best_state = child
                alpha = max(alpha, best_val)
                if alpha >= beta:
                    break
            return best_col, best_state
        else:
            best_val = float('inf')
            alpha = -float('inf')
            beta = float('inf')
            for col in state.legal_moves():
                child = state.clone_and_apply(col)
                val = AlphaBetaEngine.maxValue(child, depth-1, alpha, beta, 'O')
                if val < best_val:
                    best_val = val
                    best_col = col
                    best_state = child
                beta = min(beta, best_val)
                if alpha >= beta:
                    break
            return best_col, best_state

    @staticmethod
    def maxValue(state: Conecta4State, depth: int, alpha: float, beta: float, root_player: str) -> float:
        # root_player is the original player for which we are evaluating utility
        if state.isTerminal() or depth <= 0:
            return state.heuristicUtility(root_player)

        value = -float('inf')
        for col in state.legal_moves():
            child = state.clone_and_apply(col)
            value = max(value, AlphaBetaEngine.minValue(child, depth-1, alpha, beta, root_player))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # beta cut-off
        return value

    @staticmethod
    def minValue(state: Conecta4State, depth: int, alpha: float, beta: float, root_player: str) -> float:
        if state.isTerminal() or depth <= 0:
            return state.heuristicUtility(root_player)

        value = float('inf')
        for col in state.legal_moves():
            child = state.clone_and_apply(col)
            value = min(value, AlphaBetaEngine.maxValue(child, depth-1, alpha, beta, root_player))
            beta = min(beta, value)
            if alpha >= beta:
                break  # alpha cut-off
        return value
