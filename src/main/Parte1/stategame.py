# src/main/Parte1/stategame.py
from abc import ABC, abstractmethod
from typing import List

class StateGame(ABC):
    """ Interfaz abstracta para un juego por turnos (StateGame). """

    @classmethod
    @abstractmethod
    def start(cls):
        """Retorna el estado inicial del juego (objeto StateGame)."""
        pass

    @abstractmethod
    def actionResults(self) -> List["StateGame"]:
        """Devuelve lista de estados alcanzables desde este estado (hijos)."""
        pass

    @abstractmethod
    def isTerminal(self) -> bool:
        """Indica si el estado es terminal (fin de partida)."""
        pass

    @abstractmethod
    def toMove(self) -> str:
        """Devuelve el jugador que tiene el turno en este estado (por ejemplo 'X' o 'O')."""
        pass

    @abstractmethod
    def rival(self, player: str) -> str:
        """Retorna el rival de `player`."""
        pass

    @abstractmethod
    def heuristicUtility(self, player: str) -> int:
        """Calcula la utilidad heurística para `player` en este estado."""
        pass

    @abstractmethod
    def toString(self) -> str:
        """Devuelve una representación en texto del estado."""
        pass
