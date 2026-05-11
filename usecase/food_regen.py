from ..config import MAXPRL, MINPRL, STABILITY_FACTOR, TAU, OSCILLATION_PERCENT
import math
from ..Entities.world import World
from ..Entities.spawn_data import SpawnData
import random
from ..Entities.food import Food
from ..Entities.randomizer import Randomizer
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
    o_mode: bool = False
    c_mode: bool = False
    randomizer: Randomizer
    r: int #direction of oscillation
    f: int # 0 of oscilation
    a: float #amplitude of oscillation
    pfactor: float
    food_added: int = 0
    counter: int
    limit: int

    def __init__(self,eng_range, randomizer: Randomizer):
        self.eng_range = eng_range
        self.randomizer = randomizer
        self.limit = randomizer.base_randomizer.randint(2* TAU, 4* TAU)
        self.counter = 0

    def caculate(self, world: World):
        animal = world.get_state().animals
        avgH = world.get_state().avgH
        minH = world.get_state().minH
        maxH = world.get_state().maxH
        Nfactor = 0
        totalCombat = world.get_state().totalCombat
        if animal > 0:
            if self.c_mode: 
                Nfactor = max(0,min((totalCombat/animal)-1 - self.counter,4))
            else: 
                Nfactor = max(0,min((totalCombat/animal)-1,4))
            self.min_bound = minH * Nfactor * animal * self.stability_factor
            self.max_bound = maxH * Nfactor * animal * self.stability_factor
            self.avg_bound = avgH * Nfactor * animal * self.stability_factor
        else:
            self.min_bound = 0.0
            self.max_bound = 0.0
            self.avg_bound = 0.0
        self.prevfood = world.get_state().food
        self.set_metric_data(world, Nfactor)

    def set_metric_data(self, world: World, Nfactor: float):
        state = world.get_state()
        state.set_regen_metric_data([Nfactor, self.min_bound, self.avg_bound, self.max_bound, self.limit])

    
    def execute(self, world: World):

        if self.cooldown >= 2*TAU or self.o_mode:
             if self.cooldown >= self.limit and not self.c_mode:
                 self.c_mode = True
             ofood = self.get_ofood(world)
             self.update_cooldown(world,0)
             self.add_food(ofood, world)
             if self.cooldown <= 0:
                 self.o_mode = False
                 self.c_mode = False
                 self.limit = self.randomizer.base_randomizer.randint(2*TAU, 4*TAU)
        
        elif self.cooldown >=0 and 2*TAU > self.cooldown:
            self.o_mode = False
            food = world.get_state().food
            dfood = dfood = max(self.prevfood - food, 0)
            self.pfactor = self.get_peaceful_factor()
            nfood = math.ceil((dfood + math.ceil(self.pfactor * food)))
            self.update_cooldown(world, nfood)
            
        else:
            self.o_mode = False
            self.pfactor = 0
            self.food_added = 0
            self.update_cooldown(world,0)
        self.set_execute_data(world)

    def update_cooldown(self, world: World, nfood: float):
        if world.get_state().totalCombat <= self.min_bound:
            self.add_food(math.ceil(nfood), world)
            self.cooldown += 3
        elif (world.get_state().totalCombat > self.min_bound) and (world.get_state().totalCombat < self.avg_bound):
            self.add_food(math.ceil(0.5*nfood), world)
            self.cooldown += 1
        elif (world.get_state().totalCombat >= self.avg_bound) and (world.get_state().totalCombat < self.max_bound):
            self.add_food(math.ceil(0.25*nfood), world)
            self.cooldown -= 3
        elif (world.get_state().totalCombat >= self.max_bound):
            self.cooldown -= 5
        
    def set_execute_data(self, world: World):
        state = world.get_state()
        state.set_regen_execute_data([self.cooldown, self.pfactor, self.food_added, self.o_mode])


    
    def get_peaceful_factor(self):
        denom = TAU + self.cooldown
        if denom == 0:
            denom += 1e-5
        return self.minPRL + (self.maxPRL - self.minPRL) * min(self.cooldown, 2 * TAU) / denom

    def get_ofood(self, world: World):
        
        if not self.o_mode:
            food = world.get_state().food
            dfood = abs(food - self.prevfood)
            self.pfactor = self.get_peaceful_factor()
            self.f = math.ceil((dfood + math.ceil(self.pfactor * food)))
            self.a = math.ceil((dfood + math.ceil(self.pfactor * food)))
            self.r = self.randomizer.base_randomizer.choice([1,-1])
            self.o_mode = True
            self.counter = -1
        self.counter += 1
        self.set_amplitude()
        return max(0,math.ceil(OSCILLATION_PERCENT*self.r * self.a*math.sin(math.pi *(self.counter)/(2*TAU))+self.f))
        
    def set_amplitude(self):
        if self.counter != 0 and self.counter % TAU == 0:
            k = self.counter // TAU
            match (k % 6):
                case 1:
                    self.a += math.ceil(self.a/(2))
                case 2:
                    self.a += math.ceil(self.a/(4))
                case 3:
                    self.a += math.ceil(self.a/(8))
                case 4:
                    self.a -= math.ceil(self.a/8)
                case 5:
                    self.a -= math.ceil(self.a/(4))
                case 0:
                    self.a -= math.ceil(self.a/(2))

    def add_food(self, n: int, world: World):
        n = max(0,n)
        self.food_added = n
        for i in range(n):
            try:
                pos = world.random_empty_cell()
            except RuntimeError:
                break
            energy = self.randomizer.base_randomizer.choice(self.eng_range)
            food = Food(energy, pos)
            world.add_food(pos, food)