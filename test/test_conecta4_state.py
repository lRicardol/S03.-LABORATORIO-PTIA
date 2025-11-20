# Test/test_conecta4_state.py
import unittest
from src.main.Parte1.conecta4_state import Conecta4State

class TestConecta4State(unittest.TestCase):
    def test_initial_state(self):
        s = Conecta4State.start()
        self.assertFalse(s.isTerminal())
        self.assertEqual(s.toMove(), 'X')
        self.assertEqual(len(s.legal_moves()), 7)

    def test_apply_move(self):
        s = Conecta4State.start()
        child = s.clone_and_apply(3)
        self.assertEqual(child.board[5][3], 'X')
        self.assertEqual(child.toMove(), 'O')

if __name__ == "__main__":
    unittest.main()
