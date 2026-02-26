from .position import Position
class Food:
    energy: float
    pos: Position

    def __init__(self, energy: float, pos: Position):
        self.energy = energy
        self.pos = pos
        pass 

    def get_energy(self) -> float:
        return self.energy

    def get_pos(self) -> Position:
        return self.pos
    
    def set_energy(self, energy: float):
        self.energy = energy

    def set_pos(self, pos: Position):
        self.pos = pos

    
