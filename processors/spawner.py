import random
from typing import Optional
from ..Entities.world import World
from ..Entities.animal import Animal
from ..Entities.food import Food
from .state_updater import StateUpdater


class Spawner:
    animal_units : int
    food_units: int
    life_range: list[int]
    hit_range: list[int]
    energy_range: list[int]
    vision_range: list[int]
    max_turns: int = -1
    state_updater: StateUpdater

    def __init__(self, animal_units: int, food_units: int, 
                 life_range: list[int], hit_range: list[int],
                 energy_range: list[int], vision_range: list[int],
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
        self.state_updater = StateUpdater()

    def fill(self, world: World):
        world = self.spawn_animals(world)
        world = self.spawn_food(world)
        self.state_updater.execute(world)
        return world
        
    def spawn_animals(self, world: World):
        for i in range(self.animal_units):
            pos = world.random_empty_cell()
            hit = random.choice(self.hit_range)
            max_life = random.choice(self.life_range)
            threshold = random.choice(self.energy_range)
            vision = random.choice(self.vision_range)
            animal = Animal(hit, max_life, threshold, vision, 0, pos, lineage= i)
            animal.set_birthed(True)
            animal.set_birth_pos(pos)
            world.add_animal(pos,animal)
        return world


    def spawn_food(self, world: World):
        for i in range(self.food_units):
            pos = world.random_empty_cell()
            energy = random.choice(self.energy_range)
            food = Food(energy, pos)
            world.add_food(pos, food)
        return world
    
    def get_spawn_data(self) -> list:
        return [["#animals", self.animal_units, self.animal_units], 
                ["#food", self.food_units, self.food_units], 
                ["hit range", self.hit_range[0], self.hit_range[-1]],
                ["life range", self.life_range[0], self.life_range[-1]],
                ["vision range", self.vision_range[0], self.vision_range[-1]],
                ["energy range", self.energy_range[0], self.energy_range[-1]],
                ["max turns", self.max_turns, self.max_turns]]

        