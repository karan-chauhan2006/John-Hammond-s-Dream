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
            animal.direct_immunity.append(virus.code)
            for i in range(1,math.floor(animal.immunity)):
                s_effect_1 = str(math.floor(virus.effect+i))
                s_effect_2 = str(math.floor(virus.effect-i))
                code_1 = virus.trait[0]+s_effect_1
                code_2 = virus.trait[0]+s_effect_2
                animal.indirect_immunity.append(code_1)
                animal.indirect_immunity.append(code_2)
            match (virus.trait):
                case config.VISION:
                    if virus.effect < 0 and abs(virus.effect) > virus.trait_val:
                        animal.vision += virus.trait_val
                    else:
                        animal.vision =max(0, animal.vision - virus.effect) 
                case config.HIT:
                    if virus.effect < 0 and abs(virus.effect) > virus.trait_val:
                        animal.hit += virus.trait_val
                    else:
                        animal.hit = max(0, animal.hit - virus.effect)
                case config.LIFE:
                    pass
                case config.THRESHOLD:
                    if virus.effect < 0 and abs(virus.effect) > virus.trait_val:
                        animal.threshold += virus.trait_val
                    else:
                        animal.threshold = max(0, animal.threshold - virus.effect)
            animal.virus.remove(virus)
        elif animal.energy > virus.cost:
            virus.phase = SYMBIOSIS
            animal.energy -= virus.cost
            virus.consumed += virus.cost
        else:
            animal.life -= 1
            virus.counter -= 1
        


               