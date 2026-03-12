import math


# -------------------- MUTABLE CONSTANTS ---------------
# ------------- FEEL FREE TO PLAY AROUND WITH ----------

# ****** SPAWN DATA ******
W: int = 55
H: int = 55
TURNS: int = 10000
SEED: int = None
# [20241114, 20241116, 20241216, 20250120, 20250214, 20250505, 
# 20251007, 20251112, 20251114, 20251116, 20260120, 20260225]
ANIMAL_UNITS: int = 700
FOOD_UNITS: int = 1250
LIFE_RANGE: list[int] = [1,80]
HIT_RANGE: list[int] = [1,10]
ENERGY_RANGE: list[int] = [1,100]
VISION_RANGE: list[int] = [15,23]
# ************************
# lists in this SPAWN DATA should be of length 2
# with min value at pos 0 and max value at pos 1 

# ******* ATTACK RULE ******
VERSION = "V1"
# *************************
# possible values of version are: 
# V1, V2, V3, V4
#check doc for details

# ***** FOOD REGEN *****
STABILITY_FACTOR: float = 0.27
MAXPRL: float = 0.09
MINPRL: float = 0.01
TAU: int = 80
OSCILLATION_PERCENT: float = 1
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



# ***** INTENTS ******
ATTACK = "ATTACK"
REPRODUCE = "REPRODUCE"
MOVE = "MOVE"
# *******************

# ***** ATTACK VERSION *****
V1 = "V1"
V2 = "V2"
V3 = "V3"
V4 = "V4" 
# *************************"

