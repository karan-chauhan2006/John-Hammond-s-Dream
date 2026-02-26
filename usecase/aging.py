from ..Entities.world import World
from ..Entities.animal import Animal
class AgeUseCase: 
    def execute(self, world: World):
        animals = world.get_animal_list()
        for key in list(animals.keys()):
            animal = world.get_animal(key)
            if animal.get_cooldown_aging() == 0:
                animal.set_life(animal.get_life()-1)
            else:
                animal.set_cooldown_aging(animal.get_cooldown_aging()-1)
            if animal.get_cooldown_attack() == 0:
                continue
            else: 
                animal.set_cooldown_attack(animal.get_cooldown_attack()-1)