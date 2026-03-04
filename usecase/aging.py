from ..Entities.world import World
from ..Entities.animal import Animal
class AgeUseCase: 
    def execute(self, world: World):
        animals = world.get_animal_list()
        for key in list(animals.keys()):
            animal = world.get_animal(key)
            if animal.get_cooldown_aging() == 0:
                animal.set_life(animal.get_life()-1)
                self.update_threshold(animal)    
            else:
                animal.set_cooldown_aging(animal.get_cooldown_aging()-1)
            if animal.get_cooldown_attack() == 0:
                continue
            else: 
                animal.set_cooldown_attack(animal.get_cooldown_attack()-1)

    def update_threshold(self, animal: Animal):
        animal.divide_counter += 1
        if animal.divide_counter >= animal.life_divider:
            while animal.divide_counter >= animal.life_divider:
                animal.divide_counter -= animal.life_divider
                if animal.ate:
                    animal.threshold += animal.threshold_buffer
                else:
                    animal.threshold -= animal.threshold
            if animal.threshold <= 0:
                animal.threshold = 1
            animal.ate = False