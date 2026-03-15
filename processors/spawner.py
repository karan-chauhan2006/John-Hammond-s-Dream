import random
from typing import Optional
from ..Entities.world import World
from ..Entities.animal import Animal
from ..Entities.food import Food
from .state_updater import StateUpdater
from ..Entities.spawn_data import SpawnData
from ..Entities.genealogy import Genealogy
from ..Entities.genealogy_data import GenealogyData

class Spawner:
    spawn_data: SpawnData
    state_updater: StateUpdater
    randomizer: random.Random

    def __init__(self, spawn_data: SpawnData, randomizer: random.Random):
        self.spawn_data = spawn_data
        self.state_updater = StateUpdater()
        self.randomizer = randomizer

    def fill(self, world: World, genealogy: Genealogy):
        world, genealogy = self.spawn_animals(world, genealogy)
        world = self.spawn_food(world)
        self.state_updater.execute(world)
        return world, genealogy
        
    def spawn_animals(self, world: World, genealogy: Genealogy):
        for i in range(self.spawn_data.animal_units):
            try:
                pos = world.random_empty_cell()
            except RuntimeError:
                break
            id = genealogy.max_id + 1
            hit = self.randomizer.choice(self.spawn_data.hit_range)
            max_life = self.randomizer.choice(self.spawn_data.life_range)
            threshold = self.randomizer.choice(self.spawn_data.energy_range)
            vision = self.randomizer.choice(self.spawn_data.vision_range)
            animal = Animal(hit, max_life, threshold, vision, 0, pos, lineage= i+1, id= id)
            animal.set_birthed(True)
            animal.set_birth_pos(pos)
            world.add_animal(pos,animal)
            data = GenealogyData(Id= id, P_Id= 0, lineage= i+1, gen = 0, birth_turn=0,
                                 birth_pos= pos, hit= hit, life= max_life, 
                                 b_threshold= threshold, vision= vision)
            genealogy.add_genealogy(data)
        return world, genealogy


    def spawn_food(self, world: World):
        for i in range(self.spawn_data.food_units):
            try:
                pos = world.random_empty_cell()
            except RuntimeError:
                break
            energy = self.randomizer.choice(self.spawn_data.energy_range)
            food = Food(energy, pos)
            world.add_food(pos, food)
        return world
    
    
        