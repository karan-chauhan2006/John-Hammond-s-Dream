import random
class Randomizer:
    seed: int
    base_randomizer: random.Random
    virus_randomiser: random.Random

    def __init__(self, seed: int):
        self.seed = seed
        self.base_randomizer = random.Random(seed)
        self.virus_randomiser = random.Random(seed + 1)
