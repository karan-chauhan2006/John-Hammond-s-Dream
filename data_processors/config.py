from pathlib import Path

# **** PATHS *****
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
# ****************

# ***** DATA HANDELING *****
TURN_DATA_CLOUMNS = ["Turn", "#animals", "#food", "avgAE", "avgET", "avgH",
               "avgV", "avgML", "avgL", "avgFE", "avgGen", "maxAE", "maxET", "maxH",
               "maxV", "maxML", "maxFE", "maxGen", "minAE", "minET", "minH",
               "minV", "minML", "minFE", "minGen", "totalAE", "totalFE", 
               "totalE", "totalCombat", "Nfactor", "min_bound", "avg_bound", "max_bound",
               "cooldown", "limit", "mode", "peaceful factor", "food added", "E-indicator", "EDM", "RDM"]
GEN_DATA_COLUMNS = ["Id", "Parent Id", "Lineage", "Gen", "Birth turn", "Birth pos x", "Birth pos y", 
                    "hit", "max life", "birth threshold", "vision", "death turn", "death pos x", "death pos y",
                    "death threshold"]
PLOTS = ["turn V/S #animals, #food", "turn v/s food added","turns V/S E-estimator", "turn V/S RDM",
         "turn V/S Hit data","turn V/S max Life data", "turn V/S vision data", "turn V/S Generation data",
         "turn V/S animal energy data", "turn V/S food energy data", "turn V/S energy data", "turn V/S EDM",
         "turn V/S food regen","turn v/s cooldown", "turn v/s mode",  "NULL"]
# **************************