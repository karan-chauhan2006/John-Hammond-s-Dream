from .config import DATA
import pandas as pd
from pathlib import Path
class SpawnDataHandler: 
    name: str 

    def __init__(self):
        pass

    
    def save_spawn_data(self, spawn_data: list, path: Path):
        df = pd.DataFrame(spawn_data, columns=["Trait", "Min Val", "Max Val"])
        df.to_csv(path / "spawn_data.csv")
    