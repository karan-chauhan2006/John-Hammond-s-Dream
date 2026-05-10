import csv
from io import TextIOWrapper
from .config import DATA, TURN_DATA_CLOUMNS, CREATE_TURN_SUMMARY, TURN_TABLE, create_insert_command
from pathlib import Path
from sqlite3 import Cursor
class TurnTableHandler:
    f: TextIOWrapper
    writer: csv.writer

    def __init__(self):
        pass

    
    def create_table(self, cursor: Cursor):
        cursor.execute(CREATE_TURN_SUMMARY)

    def insert_row(self, cursor: Cursor, data: list):
        command = create_insert_command(TURN_DATA_CLOUMNS, TURN_TABLE)
        cursor.execute(command, data)