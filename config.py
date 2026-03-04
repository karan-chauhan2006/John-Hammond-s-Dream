from pathlib import Path



# -------------------- MUTABLE CONSTANTS ---------------
# ------------- FEEL FREE TO PLAY AROUND WITH ----------

# ****** SPAWN DATA ******
W: int = 40
H: int = 40
TURNS: int = 500
SEED: int = 10
ANIMAL_UNITS: int = 200
FOOD_UNITS: int = 1000
LIFE_RANGE: list[int] = [1,50]
HIT_RANGE: list[int] = [1,10]
ENERGY_RANGE: list[int] = [1,1000]
VISION_RANGE: list[int] = [10,15]
# ************************
# lists in this SPAWN DATA should be of length 2
# with min value at pos 0 and max value at pos 1 

# ***** FOOD REGEN *****
STABILITY_FACTOR: float = 0.25
MAXPRL: float = 0.4
MINPRL: float = 0.01
TAU: int = 25
OSCILLATION_PERCENT: float = 0.15
# **********************

# ***** REPRODUCTION & MUTATION ******
REPRODUCTION_CONSTANT: float|int = 4
MUTATION_CONSTANT: float = 0.01
MUTATION_CHOICE: list[int] = [-1,0,1] 
LIFE_DIVIDER: int = 10
# ***********************************
# For MUTATION_CHOICE, It is advised to keep the list
# in increasing order, and to keep all ints between min
# and max

# -------------------IMMUTABLE CONSTANTS-----------------------
# ---------------------DO NOT CHANGE---------------------------

# **** PATHS *****
ROOT = Path(__file__).resolve().parents[0]
DATA = ROOT / "data"
RAW_DATA = DATA / "raw"
PLOT_DATA = DATA / "plot"
# ****************

# ***** DATA HANDELING *****
CLOUMNS = ["Turn", "#animals", "#food", "avgAE", "avgET", "avgH",
               "avgV", "avgML", "avgL", "avgFE", "avgGen", "maxAE", "maxET", "maxH",
               "maxV", "maxML", "maxFE", "maxGen", "minAE", "minET", "minH",
               "minV", "minML", "minFE", "minGen", "totalAE", "totalFE", 
               "totalE", "totalCombat"]
PLOTS = ["turn V/S #animals, #food & total Combat", "turn V/S animal energy data & energy threshold data", "turn V/S Hit data",
                                            "turn V/S max Life data", "turn V/S vision data", "turn V/S Generation data",
                                            "turn V/S food energy data", "turn V/S energy data", "turn V/S food regen"]
# **************************

# ***** INTENTS ******
ATTACK = "ATTACK"
REPRODUCE = "REPRODUCE"
MOVE = "MOVE"
# *******************



