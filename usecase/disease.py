from ..Entities.world import World
from ..Entities.animal import Animal
from ..Entities.virus import Virus
from .config import SYMBIOSIS, LETHAL
from . import config
import math
class DiseaseUseCase: 

    def execute(self, world: World):
        animal = world.get_animal_list()
        for animal in list(animal.values()):
           if animal.has_virus():
               for virus in animal.virus:
                   if virus.phase is SYMBIOSIS:
                       self.symbiosis_infection(animal, virus)
                   else:
                       self.lethal_infection(animal, virus)

    def symbiosis_infection(self, animal: Animal, virus: Virus):
        if animal.energy < virus.cost:
            virus.phase = LETHAL
            virus.counter += math.floor(virus.consumed/virus.factor)
            animal.life -= 1
        else:
            animal.energy -= virus.cost
            virus.consumed += virus.cost
    
    def lethal_infection(self, animal: Animal, virus: Virus):
        if virus.counter == 0:
            match (virus.trait):
                case config.VISION:
                    animal.vision = virus.trait_val
                case config.HIT:
                    animal.hit = virus.trait_val
                case config.LIFE:
                    pass
                case config.THRESHOLD:
                    animal.threshold = virus.trait_val
            animal.virus.remove(virus)
        elif animal.energy > virus.cost:
            virus.phase = SYMBIOSIS
            animal.energy -= virus.cost
            virus.consumed += virus.cost
        else:
            animal.life -= 1
            virus.counter -= 1
        


               