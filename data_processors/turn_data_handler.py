import csv
from io import TextIOWrapper
from .config import DATA, CLOUMNS
from pathlib import Path
class TurnDataHandler:
    f: TextIOWrapper
    writer: csv.writer

    def __init__(self):
        pass

    def start_record(self, path: Path):
        self.f = open(path / "turn_data.csv", "w", newline= "")
        self.writer = csv.writer(self.f)
        self.writer.writerow(CLOUMNS)

    def record_data(self, data: list):
        self.writer.writerow(data)

    def end_record(self):
        self.f.close()
    
