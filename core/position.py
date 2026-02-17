from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def get_x(self) -> int:
        return self.x
    
    def get_y(self)-> int:
        return self.y

    def neighbours(self) -> list["Position"]:
        return [
            Position(self.x - 1, self.y),
            Position(self.x + 1, self.y),
            Position(self.x, self.y - 1),
            Position(self.x, self.y + 1),
        ]
    
    def neighbours_x(self) -> list["Position"]:
        return [
            Position(self.x - 1, self.y),
            Position(self.x + 1, self.y),
        ]
    
    def neighbours_y(self) -> list["Position"]:
        return [
            Position(self.x, self.y - 1),
            Position(self.x, self.y + 1),
        ]
    