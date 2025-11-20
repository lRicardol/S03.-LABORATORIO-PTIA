# src/main/Parte1/play_demo.py
from conecta4_state import Conecta4State
from alpha_beta_engine import AlphaBetaEngine

def demo_play(depth=4):
    state = Conecta4State.start()
    print("Estado inicial:")
    state.pretty_print()

    # Demo: realizar 6 jugadas (X then O then X...) usando el motor para X y O
    for turn in range(8):
        if state.isTerminal():
            print("Estado terminal alcanzado.")
            break
        print(f"\nTurno {turn+1} - juega: {state.toMove()}")
        col, child = AlphaBetaEngine.search(state, depth)
        if col == -1:
            print("No hay movimientos legales.")
            break
        print(f"Engine elige columna {col}")
        state = child
        state.pretty_print()
        w = state.winner()
        if w:
            print(f"\nGanador: {w}")
            break

if __name__ == "__main__":
    demo_play(depth=4)
