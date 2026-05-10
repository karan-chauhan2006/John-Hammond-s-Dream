from pathlib import Path

# **** PATHS *****
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
# ****************

# ***** DATA HANDELING *****
TURN_DATA_CLOUMNS = ["Turn", "num_animals", "num_food", "avgAE", "avgET", "avgH",
               "avgV", "avgImm", "avgML", "avgL", "avgFE", "avgGen", "maxAE", "maxET", "maxH",
               "maxV", "maxImm", "maxML", "maxFE", "maxGen", "minAE", "minET", "minH",
               "minV", "minImm", "minML", "minFE", "minGen", "totalAE", "totalFE", 
               "totalE", "totalCombat", "Nfactor", "min_bound", "avg_bound", "max_bound",
               "cooldown", "cycle_limit", "mode", "peaceful_factor", "food_added", "E_indicator", "EDM", "RDM"]
GEN_DATA_COLUMNS = ["animal_id", "parent_id", "Lineage", "Gen", "Birth_turn", "Birth_pos_x", "Birth_pos_y", 
                    "hit", "max_life", "birth_threshold", "vision", "death_turn", "death_pos_x", "death_pos_y",
                    "death_threshold"]
SPAWN_DATA_COLUMNS = ["Trait", "Min_Val", "Max_Val"]
PLOTS = ["turn V/S #animals, #food", "turn v/s food added","turns V/S E-estimator", "turn V/S RDM",
         "turn V/S Hit data","turn V/S max Life data", "turn V/S vision data", "turn V/S Generation data",
         "turn V/S animal energy data", "turn V/S food energy data", "turn V/S energy data", "turn V/S EDM",
         "turn V/S food regen","turn v/s cooldown", "turn v/s mode",  "turn v/s animal threshold data"]
# **************************

#********** TABLE NAME *******
GENEALOGY_TABLE = "genealogy"
SPAWN_TABLE = "spawn_data"
TURN_TABLE = "turn_summary"
#*****************************

# ********* SQL COMMANDS ********

CREATE_GENEALOGY = f"""
                    CREATE TABLE IF NOT EXISTS {GENEALOGY_TABLE} (
                                animal_id INTEGER PRIMARY KEY, 
                                parent_id INTEGER,
                                Lineage INTEGER, 
                                Gen INTEGER, 
                                Birth_turn INTEGER, 
                                Birth_pos_x INTEGER, 
                                Birth_pos_y INTEGER, 
                                hit REAL, 
                                max_life INTEGER, 
                                birth_threshold REAL, 
                                vision REAL, 
                                death_turn INTEGER, 
                                death_pos_x INTEGER, 
                                death_pos_y INTEGER,
                                death_threshold REAL)
                    """

CREATE_SPAWN = f"""
        CREATE TABLE IF NOT EXISTS {SPAWN_TABLE} (
                    Trait TEXT PRIMARY KEY,
                    Min_Val TEXT, 
                    Max_Val TEXT)
        """

CREATE_TURN_SUMMARY = f"""
        CREATE TABLE IF NOT EXISTS {TURN_TABLE} (
                    Turn INTEGER PRIMARY KEY, 
                    num_animals INTEGER, 
                    num_food INTEGER, 
                    avgAE REAL, 
                    avgET REAL, 
                    avgH REAL,
                    avgV REAL, 
                    avgML REAL, 
                    avgL REAL, 
                    avgFE REAL, 
                    avgGen REAL, 
                    maxAE REAL, 
                    maxET REAL, 
                    maxH REAL,
                    maxV REAL, 
                    maxML REAL, 
                    maxFE REAL, 
                    maxGen REAL, 
                    minAE REAL, 
                    minET REAL, 
                    minH REAL,
                    minV REAL, 
                    minML REAL, 
                    minFE REAL,
                    minGen REAL, 
                    totalAE REAL, 
                    totalFE REAL, 
                    totalE REAL, 
                    totalCombat REAL, 
                    Nfactor REAL, 
                    min_bound REAL, 
                    avg_bound REAL, 
                    max_bound REAL,
                    cooldown REAL, 
                    cycle_limit REAL, 
                    mode TEXT, 
                    peaceful_factor REAL, 
                    food_added REAL, 
                    E_indicator REAL, 
                    EDM REAL, 
                    RDM REAL)
        """

# ********** HELPER *******

def create_insert_command(column_header: list[str], table_name: str) -> str:
    columns = ""
    placeholder = ""
    for head in column_header:
        if head == column_header[-1]:
            columns += head
            placeholder += "?"
        else:
            columns += head + ","
            placeholder += "?,"
    return f"""
            INSERT INTO {table_name} ({columns})
            VALUES ({placeholder})
    """