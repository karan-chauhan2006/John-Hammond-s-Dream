import csv
from io import TextIOWrapper
from pathlib import Path
from .config import GEN_DATA_COLUMNS
class GenealogyDataHandler: 
    f: TextIOWrapper
    writer: csv.writer

    def __init__(self):
        pass

    def start_record(self, path: Path):
        self.f = open(path / "genealogy_data.csv", "w", newline= "")
        self.writer = csv.writer(self.f)
        self.writer.writerow(GEN_DATA_COLUMNS)

    def record_data(self, data: list):
        self.writer.writerow(data)

    def end_record(self):
        self.f.close()