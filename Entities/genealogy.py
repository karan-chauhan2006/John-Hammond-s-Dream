from .genealogy_data import GenealogyData
from ..Entities.position import Position
class Genealogy:
    live_genes: dict[int, GenealogyData]
    dead_genes: dict[int, GenealogyData]
    max_id: int 

    def __init__(self):
        self.live_genes = {}
        self.dead_genes = {}
        self.max_id = 0

    def add_genealogy(self, data: GenealogyData):
        self.live_genes[data.Id] = data
        self.max_id += 1

    def finalise_genealogy(self, Id: int, death_turn: int, death_pos: Position, d_threshold: float):
        data = self.live_genes.pop(Id)
        data.set_final_data(death_turn, death_pos, d_threshold)
        self.dead_genes[Id] = data

    def empty_genes(self) -> dict[int, GenealogyData]:
        data = self.dead_genes
        self.dead_genes = {}
        return data
