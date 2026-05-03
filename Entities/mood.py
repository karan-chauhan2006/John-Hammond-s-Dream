from .position import Position
class Mood:
    type: str
    target: object
    start: Position

    def __init__(self, type: str, target: object, start: Position):
        self.type = type
        self.target = target
        self.start = start