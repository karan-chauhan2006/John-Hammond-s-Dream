from .spawn_data_handler import SpawnDataHandler
from .turn_data_handler import TurnDataHandler
from .config import DATA
from pathlib import Path
from ..Entities.spawn_data import SpawnData
from ..Entities.state import State
class DataHandler:
    file_path: Path 
    spawn_data_handler: SpawnDataHandler
    turn_data_handler: TurnDataHandler

    def __init__(self, name: str):
        self.file_path = DATA / name
        self.spawn_data_handler = SpawnDataHandler()
        self.turn_data_handler = TurnDataHandler()

    def start(self):
        self.file_path.mkdir()
        self.turn_data_handler.start_record(self.file_path)

    def record_spawn_data(self, spawn_data: SpawnData):
        self.spawn_data_handler.save_spawn_data(spawn_data, self.file_path)

    def record_turn_data(self, state: State):
        data = state.get_arr()
        self.turn_data_handler.record_data(data)

    def close(self):
        self.turn_data_handler.end_record()
        
