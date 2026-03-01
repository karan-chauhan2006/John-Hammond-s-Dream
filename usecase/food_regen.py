from ..config import MAXPRL, MINPRL, STABILITY_FACTOR, TAU
import math
from ..Entities.world import World
from ..Entities.spawn_data import SpawnData
import random
from ..Entities.food import Food
class FoodRegenUseCase:
    stability_factor = STABILITY_FACTOR
    maxPRL = MAXPRL
    minPRL = MINPRL
    min_bound: float = 0.0
    avg_bound: float = 0.0
    max_bound: float = 0.0
    cooldown: int = 0
    prevfood: int = 0
    eng_range: list 

    def __init__(self,eng_range):
        self.eng_range = eng_range

    def caculate(self, world: World):
        animal = world.get_state().animals
        avgH = world.get_state().avgH
        minH = world.get_state().minH
        maxH = world.get_state().maxH
        totalCombat = world.get_state().totalCombat
        if animal > 0:
            Nfactor = totalCombat/animal
            self.min_bound = minH * (math.floor(Nfactor)-1) * animal * self.stability_factor
            self.max_bound = maxH * (math.floor(Nfactor)-1) * animal * self.stability_factor
            self.avg_bound = avgH * (math.floor(Nfactor)-1) * animal * self.stability_factor
        else:
            self.min_bound = 0.0
            self.max_bound = 0.0
            self.avg_bound = 0.0
        self.prevfood = world.get_state().food
    
    def execute(self, world: World):
        food = world.get_state().food
        dfood = math.fabs(food - self.prevfood)
        pfactor = self.get_peaceful_factor()
        animal = world.get_state().animals
        maxSpace = (world.get_space()) - animal - food - math.ceil(0.05*world.get_space()) 
        nfood = min(dfood + math.ceil(pfactor * food), maxSpace)

        if self.cooldown <=0:
            if world.get_state().totalCombat < self.min_bound or self.min_bound <= 0:
                self.add_food(math.ceil(nfood), world)
                self.cooldown -= 1
            elif (world.get_state().totalCombat >= self.min_bound) and (world.get_state().totalCombat < self.avg_bound):
                self.add_food(math.ceil(0.5*nfood), world)
                self.cooldown -= 1
            elif (world.get_state().totalCombat >= self.avg_bound) and (world.get_state().totalCombat < self.max_bound):
                self.add_food(math.ceil(0.25*nfood), world)
                self.cooldown += 3
            elif (world.get_state().totalCombat >= self.max_bound):
                self.cooldown += 5
        else:
            if world.get_state().totalCombat < self.min_bound or self.min_bound <= 0:
                self.cooldown -= 5
            elif world.get_state().totalCombat >= self.min_bound and world.get_state().totalCombat < self.avg_bound:
                self.cooldown -= 3
            elif world.get_state().totalCombat >= self.avg_bound and world.get_state().totalCombat < self.max_bound:
                self.cooldown += 1
            elif world.get_state().totalCombat >= self.max_bound:
                self.cooldown += 2

    
    def get_peaceful_factor(self):
        if TAU - self.cooldown == 0:
            return self.minPRL + (self.maxPRL - self.minPRL)*(-self.cooldown)/(TAU - self.cooldown + 10e-5)
        else:
            return self.minPRL + (self.maxPRL - self.minPRL)*(-self.cooldown)/(TAU - self.cooldown)
        
    def add_food(self, n: int, world: World):
        for i in range(n):
            pos = world.random_empty_cell()
            energy = random.choice(self.eng_range)
            food = Food(energy, pos)
            world.add_food(pos, food)