import csv
from io import TextIOWrapper
from pathlib import Path
from sqlite3 import Cursor
from .config import GEN_DATA_COLUMNS, CREATE_GENEALOGY, GENEALOGY_TABLE, create_insert_command
class GenealogyTableHandler: 
    f: TextIOWrapper
    writer: csv.writer

    def __init__(self):
        pass

    def create_table(self, cursor: Cursor):
        cursor.execute(CREATE_GENEALOGY)

    def insert_row(self, cursor: Cursor, data: list):
        command = create_insert_command(GEN_DATA_COLUMNS, GENEALOGY_TABLE)
        cursor.execute(command, data)
        