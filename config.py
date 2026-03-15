import math


# -------------------- MUTABLE CONSTANTS ---------------
# ------------- FEEL FREE TO PLAY AROUND WITH ----------

# ****** SPAWN DATA ******
W: int = 35
H: int = 35
TURNS: int = 10000
SEED: int = None
# [20241114, 20241116, 20241216, 20250120, 20250214, 20250505, 
# 20251007, 20251112, 20251114, 20251116, 20260120, 20260225]
ANIMAL_UNITS: int = 245
FOOD_UNITS: int = 735
LIFE_RANGE: list[int] = [1,60]
HIT_RANGE: list[int] = [1,15]
ENERGY_RANGE: list[int] = [1,150]
VISION_RANGE: list[int] = [6,14]
# ************************
# lists in this SPAWN DATA should be of length 2
# with min value at pos 0 and max value at pos 1 

# ******* ATTACK RULE ******
VERSION = "V1"
# *************************
# possible values of version are: 
# V1, V2, V3, V4, V5
#check doc for details

# ***** FOOD REGEN *****
STABILITY_FACTOR: float = 0.5
MAXPRL: float = 0.09
MINPRL: float = 0.01
TAU: int = 100
OSCILLATION_PERCENT: float = 0.25
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





