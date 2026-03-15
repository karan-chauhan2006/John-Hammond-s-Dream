from .spawn_data_handler import SpawnDataHandler
from .turn_data_handler import TurnDataHandler
from .geneaology_data_handler import GenealogyDataHandler
from .config import DATA
from pathlib import Path
from ..Entities.spawn_data import SpawnData
from ..Entities.state import State
from ..Entities.genealogy_data import GenealogyData
class DataHandler:
    file_path: Path 
    spawn_data_handler: SpawnDataHandler
    turn_data_handler: TurnDataHandler
    genealogy_data_handler: GenealogyDataHandler

    def __init__(self, name: str):
        self.file_path = DATA / name
        self.spawn_data_handler = SpawnDataHandler()
        self.turn_data_handler = TurnDataHandler()
        self.genealogy_data_handler = GenealogyDataHandler()

    def start(self):
        self.file_path.mkdir()
        self.turn_data_handler.start_record(self.file_path)
        self.genealogy_data_handler.start_record(self.file_path)

    def record_spawn_data(self, spawn_data: SpawnData):
        self.spawn_data_handler.save_spawn_data(spawn_data, self.file_path)

    def record_turn_data(self, state: State):
        self.turn_data_handler.record_data(state.get_arr())

    def record_gen_data(self, genes: dict[int, GenealogyData]):
        for id in list(genes.keys()):
            self.genealogy_data_handler.record_data(genes[id].get_data())

    def close(self):
        self.turn_data_handler.end_record()
        self.genealogy_data_handler.end_record()
        
