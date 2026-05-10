from .config import DATA, CREATE_SPAWN, SPAWN_TABLE, SPAWN_DATA_COLUMNS, create_insert_command
import pandas as pd
from sqlite3 import Cursor
from pathlib import Path
class SpawnTableHandler: 
    name: str 

    def __init__(self):
        pass

    
    def create_table(self, cursor: Cursor):
        cursor.execute(CREATE_SPAWN)
    
    def insert_rows(self, cursor: Cursor, data: list):
        command = create_insert_command(SPAWN_DATA_COLUMNS, SPAWN_TABLE)
        cursor.executemany(command, data)