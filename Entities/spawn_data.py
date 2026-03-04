from typing import Optional
from ..config import MUTATION_CONSTANT, STABILITY_FACTOR, MAXPRL
from ..config import MINPRL, TAU, REPRODUCTION_CONSTANT, MUTATION_CHOICE
class SpawnData:
    animal_units : int
    food_units: int
    life_range: list[float]
    hit_range: list[float]
    energy_range: list[float]
    vision_range: list[float]
    max_turns: int = -1

    def __init__(self, animal_units: int, food_units: int, 
                 life_range: list[float], hit_range: list[float],
                 energy_range: list[float], vision_range: list[float],
                 max_turns: Optional[int]=-1):
        self.animal_units = animal_units
        self.food_units = food_units
        self.life_range = []
        for i in range(life_range[1]-life_range[0]):
            self.life_range.append(life_range[0]+i)
        self.hit_range = []
        for i in range(hit_range[1]-hit_range[0]):
            self.hit_range.append(hit_range[0]+i)
        self.energy_range = []
        for i in range(energy_range[1]-energy_range[0]):
            self.energy_range.append((float)(energy_range[0]+i))
        self.vision_range = []
        for i in range(vision_range[1]-vision_range[0]):
            self.vision_range.append(vision_range[0]+i)
        self.max_turns = max_turns
    
    def get_data(self, W: int, H: int) -> list:
        return [["#animals", self.animal_units, self.animal_units], 
                ["#food", self.food_units, self.food_units], 
                ["hit range", self.hit_range[0], self.hit_range[-1]],
                ["life range", self.life_range[0], self.life_range[-1]],
                ["vision range", self.vision_range[0], self.vision_range[-1]],
                ["energy range", self.energy_range[0], self.energy_range[-1]],
                ["max turns", self.max_turns, self.max_turns],
                ["Map Width", W, W],
                ["Map Height", H, H],
                ["Peace Regen Limit", MINPRL, MAXPRL],
                ["Stability factor", STABILITY_FACTOR, STABILITY_FACTOR],
                ["Half cycle", TAU, TAU],
                ["Mutation constant", MUTATION_CONSTANT, MUTATION_CONSTANT],
                ["Mutation Choice", MUTATION_CHOICE[0], MUTATION_CHOICE[-1]]]
    
    def get_mutate_list(self):
        #HLTV
        
        return [(self.hit_range[-1]-self.hit_range[0]+2)*MUTATION_CONSTANT,
                (self.life_range[-1]-self.life_range[0]+2)*MUTATION_CONSTANT,
                (self.energy_range[-1]-self.energy_range[0]+2)*MUTATION_CONSTANT,
                (self.vision_range[-1]-self.vision_range[0]+2)*MUTATION_CONSTANT]
    
    def get_eng_list(self):
        return self.energy_range
