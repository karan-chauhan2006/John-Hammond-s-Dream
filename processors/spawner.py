import random
from typing import Optional
from ..Entities.world import World
from ..Entities.animal import Animal
from ..Entities.food import Food
from .state_updater import StateUpdater
from ..Entities.spawn_data import SpawnData

class Spawner:
    spawn_data: SpawnData
    state_updater: StateUpdater

    def __init__(self, spawn_data: SpawnData):
        self.spawn_data = spawn_data
        self.state_updater = StateUpdater()

    def fill(self, world: World):
        world = self.spawn_animals(world)
        world = self.spawn_food(world)
        self.state_updater.execute(world)
        return world
        
    def spawn_animals(self, world: World):
        for i in range(self.spawn_data.animal_units):
            pos = world.random_empty_cell()
            hit = random.choice(self.spawn_data.hit_range)
            max_life = random.choice(self.spawn_data.life_range)
            threshold = random.choice(self.spawn_data.energy_range)
            vision = random.choice(self.spawn_data.vision_range)
            animal = Animal(hit, max_life, threshold, vision, 0, pos, lineage= i)
            animal.set_birthed(True)
            animal.set_birth_pos(pos)
            world.add_animal(pos,animal)
        return world


    def spawn_food(self, world: World):
        for i in range(self.spawn_data.food_units):
            pos = world.random_empty_cell()
            energy = random.choice(self.spawn_data.energy_range)
            food = Food(energy, pos)
            world.add_food(pos, food)
        return world
    
    
        