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

    def lookup(self, id: int) -> int|None:
        try: 
            parent_id = self.live_genes[id].P_Id
            if parent_id == 0:
                return id
            else:
                ans = self.lookup(parent_id)
                if ans is None:
                    return id
                else:
                    return ans
        except KeyError:
            return None 
    
    def is_alive(self, id: int) -> bool:
        try: 
            animal = self.live_genes[id]
            return True
        except KeyError:
            return False
            
