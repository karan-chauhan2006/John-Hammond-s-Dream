import pandas as pd
from ..Entities.state import State
from datetime import datetime
from pathlib import Path
from ..config import RAW_DATA, CLOUMNS
class DataHandler: 
    data = list[list]
    columns = CLOUMNS
    
    def __init__(self):
        self.data = []

    def save_state(self, state: State):
        self.data.append(state.get_arr())
        
    def save_data(self, spawn_data: list) -> Path:
        path = self.create_dir()
        self.save_spawn_data(path, spawn_data)
        self.save_turn_data(path)
        self.save_gen_data(path)
        return path
    
    def create_dir(self) -> Path:
        now = datetime.now()
        name = now.strftime("%Y_%m_%d_%H_%M_%S")
        (RAW_DATA / name).mkdir()
        return RAW_DATA / name
    
    def save_spawn_data(self, path: Path, spawn_data: list):
        df = pd.DataFrame(spawn_data, columns=["Trait", "Min Val", "Max Val"])
        df.to_csv(path / "spawn_data.csv")

    def save_turn_data(self, path: Path):
        df = pd.DataFrame(self.data, columns= self.columns)
        df.to_csv(path / "turn_data.csv", index=False)

    def save_gen_data(self, path: Path):
        pass
