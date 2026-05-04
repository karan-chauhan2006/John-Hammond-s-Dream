from ..Entities.food import Food
from ..Entities.world import World
from ..Entities.virus import Virus
from . import config
from ..config import ENERGY_RANGE, HIT_RANGE, VISION_RANGE, LIFE_RANGE
import random
class VirusSpawnUseCase:
    randomizer: random.Random 

    def __init__(self, randomizer: random.Random):
        self.randomizer = randomizer
        pass

    def execute(self, world: World):
        foods = world.get_food_list()
        for food in list(foods.values()):
            if food.has_virus():
                continue
            else:
                if self.check(food):
                    self.spawn_virus(food)

    def check(self, food: Food) -> bool:
        ratio = food.get_energy() / food.max_energy
        choice = self.randomizer.choice([1,0,-1])
        return (ratio < 0.7) and (0.5 < ratio ) and (choice == 1)
    
    def spawn_virus(self, food: Food):
        food.energy -= 3
        effect = self.get_effect(food.type)
        cost = self.get_cost(effect, food.type)
        virus = Virus(food.type, effect, 0.5 * food.max_energy, cost)
        food.virus.append(virus)

    def get_effect(self, trait: str):
        match trait:
            case config.VISION:
                mag = self.randomizer.randint(1, VISION_RANGE[1]-VISION_RANGE[0]) 
            case config.HIT:
                mag = self.randomizer.randint(1, HIT_RANGE[1]-HIT_RANGE[0])
            case config.LIFE:
                mag = self.randomizer.randint(1, LIFE_RANGE[1]-LIFE_RANGE[0])
            case config.THRESHOLD:
                mag = self.randomizer.randint(1, ENERGY_RANGE[1]-ENERGY_RANGE[0])
        sgn = self.randomizer.choice([1,-1])
        return mag * sgn
    
    def get_cost(self, effect: float, type: str)-> float:
         effect = abs(effect)
         match type:
            case config.VISION:
                rat = (effect)/ (VISION_RANGE[0]-VISION_RANGE[1])
            case config.HIT:
               rat = (effect)/ (HIT_RANGE[0]-HIT_RANGE[1])
            case config.LIFE:
                rat = (effect)/ (LIFE_RANGE[0]-LIFE_RANGE[1])
            case config.THRESHOLD:
                rat = (effect)/ (ENERGY_RANGE[0]-ENERGY_RANGE[1])
         return rat * (ENERGY_RANGE[0]-ENERGY_RANGE[1]) / 10




        

