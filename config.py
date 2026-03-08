from pathlib import Path
import math


# -------------------- MUTABLE CONSTANTS ---------------
# ------------- FEEL FREE TO PLAY AROUND WITH ----------

# ****** SPAWN DATA ******
W: int = 50
H: int = 50
TURNS: int = 10000
SEED: int = 20260607
ANIMAL_UNITS: int = 750
FOOD_UNITS: int = 1250
LIFE_RANGE: list[int] = [1,50]
HIT_RANGE: list[int] = [1,10]
ENERGY_RANGE: list[int] = [1,100]
VISION_RANGE: list[int] = [15,23]
# ************************
# lists in this SPAWN DATA should be of length 2
# with min value at pos 0 and max value at pos 1 

# ***** FOOD REGEN *****
STABILITY_FACTOR: float = 0.19
MAXPRL: float = 0.09
MINPRL: float = 0.01
TAU: int = 150
OSCILLATION_PERCENT: float = 0.1
# **********************

# ***** REPRODUCTION & MUTATION ******
REPRODUCTION_CONSTANT: float|int = 4
MUTATION_CONSTANT: float = 0.01
MUTATION_CHOICE: list[int] = [-1,0,1] 
LIFE_DIVIDER: int = 5
# ***********************************
# For MUTATION_CHOICE, It is advised to keep the list
# in increasing order, and to keep all ints between min
# and max

# -------------------IMMUTABLE CONSTANTS-----------------------
# ---------------------DO NOT CHANGE---------------------------

# **** PATHS *****
ROOT = Path(__file__).resolve().parents[0]
DATA = ROOT / "data"
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



