from .position import Position
class GenealogyData: 
    Id: int
    P_Id: int
    lineage: int
    gen: int
    birth_turn: int
    birth_pos: Position
    hit: float
    life: float
    b_threshold: float
    vision: float
    death_turn: int = -1
    death_pos: Position = Position(None, None)
    d_thereshold: float = -1

    def __init__(self, Id: int, P_Id: int, lineage: int, gen: int,
                  birth_turn: int, birth_pos: Position, hit: float,
                  life: float, b_threshold: float, vision: float):
        self.Id = Id
        self.P_Id = P_Id
        self.lineage = lineage
        self.gen = gen
        self.birth_turn = birth_turn
        self.birth_pos = birth_pos
        self.hit = hit
        self.life = life
        self.b_threshold = b_threshold
        self.vision = vision

    def set_final_data(self, death_turn: int, death_pos: Position, d_threshold: float):
        self.death_turn = death_turn
        self.death_pos = death_pos
        self.d_thereshold = d_threshold

    def get_data(self) -> list:
        return [self.Id, self.P_Id, self.lineage, self.gen, 
                self.birth_turn, self.birth_pos.x, self.birth_pos.y, self.hit, self.life,
                self.b_threshold, self.vision, self.death_turn, self.death_pos.x, self.death_pos.y,
                self.d_thereshold]