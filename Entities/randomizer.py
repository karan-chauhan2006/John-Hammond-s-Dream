import random
class Randomizer:
    seed: int
    base_randomizer: random.Random

    def __init__(self, seed: int):
        self.seed = seed
        self.base_randomizer = random.Random(seed)
