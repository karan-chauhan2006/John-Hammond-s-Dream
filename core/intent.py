from .position import Position
class Intent: 
    kind: str
    target: Position = None

    def __init__(self, kind: str, target: Position):
        self.kind = kind
        self.target = target

    def get_kind(self) -> str:
        return self.kind
    
    def get_target(self) -> Position:
        return self.target
    
    def set_kind(self, kind: str):
        self.kind = kind

    def set_target(self, target: Position):
        self.target = target

