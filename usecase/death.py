from ..Entities.world import World
from ..Entities.animal import Animal
from ..Entities.food import Food
from ..Entities.genealogy import Genealogy
from ..Entities.genealogy_data import GenealogyData
from .config import TRAITS
import random
class DeathUseCase: 
    randomizer: random.Random

    def __init__(self, randomizer: random.Random):
        self.randomizer = randomizer

    def execute(self, world: World, genealogy: Genealogy):
        animals = world.get_animal_list()
        for key in list(animals.keys()):
            animal = world.get_animal(key)
            if animal.get_life() <= 0:
                energy = animal.get_energy()
                world.remove_animal(key)
                type = self.randomizer.choice(TRAITS)
                food = Food(energy, key, type)
                world.add_food(key, food)
                genealogy.finalise_genealogy(animal.Id, world.get_state().turn, animal.pos, animal.threshold) 

    
                       