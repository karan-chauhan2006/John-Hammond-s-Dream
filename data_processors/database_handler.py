from .spawn_table_handler import SpawnTableHandler
from .turn_table_handler import TurnTableHandler
from .geneaology_table_handler import GenealogyTableHandler
from .config import DATA
from pathlib import Path
from ..Entities.spawn_data import SpawnData
from ..Entities.state import State
from ..Entities.genealogy_data import GenealogyData
import sqlite3
class DataBaseHandler:
    file_path: Path 
    spawn_table_handler: SpawnTableHandler
    turn_table_handler: TurnTableHandler
    genealogy_table_handler: GenealogyTableHandler
    data_base: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, name: str):
        self.file_path = DATA / name
        self.spawn_table_handler = SpawnTableHandler()
        self.turn_table_handler = TurnTableHandler()
        self.genealogy_table_handler = GenealogyTableHandler()

    def start(self):
        self.file_path.mkdir(parents=True, exist_ok=True)
        self.data_base = sqlite3.connect(self.file_path / "data_base.db")
        self.cursor = self.data_base.cursor()
        self.spawn_table_handler.create_table(self.cursor)
        self.turn_table_handler.create_table(self.cursor)
        self.genealogy_table_handler.create_table(self.cursor)
        self.data_base.commit()

    def record_spawn_data(self, spawn_data: SpawnData):
        self.spawn_table_handler.insert_rows(self.cursor, spawn_data)
        self.data_base.commit()

    def record_turn_data(self, state: State):
        self.turn_table_handler.insert_row(self.cursor, state.get_arr())
        self.data_base.commit()

    def record_gen_data(self, genes: dict[int, GenealogyData]):
        for genData in list(genes.values()):
            self.genealogy_table_handler.insert_row(self.cursor, genData.get_data())
        self.data_base.commit()

    def close(self):
        self.data_base.commit()
        self.cursor.close()
        self.data_base.close()
        
