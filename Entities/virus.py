import math
class Virus:
    trait: str
    effect: float
    trait_val: float
    consumed: float
    factor: float
    counter: int
    cost: float
    phase: str 
    code: str

    def __init__(self, trait: str, effect: float, factor: float, cost: float):
        self.trait = trait
        self.effect = effect
        self.factor = factor
        self.trait_val = 0.0
        self.consumed = 0.0
        self.counter = 0
        self.phase = None
        self.cost = cost
        self.set_code(trait, effect)

    def infected(self, trait_val: float):
        self.trait_val = trait_val

    def set_code(self, trait:str, effect:float):
        s_effect = str(math.floor(effect))
        self.code = trait[0] + s_effect
