from .position import Position
from .virus import Virus
class Food:
    max_energy: float
    energy: float
    pos: Position
    type: str
    virus: list[Virus]

    def __init__(self, energy: float, pos: Position, type: str):
        self.max_energy = energy
        self.energy = energy
        self.pos = pos
        self.type = type
        self.virus = []
        pass 

    def get_energy(self) -> float:
        return self.energy

    def get_pos(self) -> Position:
        return self.pos
    
    def set_energy(self, energy: float):
        self.energy = energy

    def set_pos(self, pos: Position):
        self.pos = pos

    def has_virus(self) -> bool: 
        return len(self.virus) != 0

    
