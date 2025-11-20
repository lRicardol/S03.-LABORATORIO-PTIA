# Test/test_alpha_beta.py
import unittest
from src.main.Parte1.conecta4_state import Conecta4State
from src.main.Parte1.alpha_beta_engine import AlphaBetaEngine

class TestAlphaBeta(unittest.TestCase):
    def test_search_returns_move(self):
        s = Conecta4State.start()
        col, child = AlphaBetaEngine.search(s, depth=2)
        self.assertIn(col, range(7))

if __name__ == "__main__":
    unittest.main()
