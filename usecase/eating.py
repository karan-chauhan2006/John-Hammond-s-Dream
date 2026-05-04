from ..Entities.world import World
from ..Entities.animal import Animal
from ..Entities.food import Food
from . import config
from .config import  SYMBIOSIS
class EatUseCase:

    def execute(self, world: World):
        foods = world.get_food_list()
        for key in list(foods.keys()):
            if world.has_animal(key):
                animal = world.get_animal(key)
                food = world.get_food(key)
                self.eat(animal, food)
                if food.has_virus():
                    self.infect(animal, food)
                world.remove_food(key)
            else:
                continue
        
    def eat(self, animal: Animal, food: Food):
        energy = animal.get_energy()
        animal.set_energy(energy + food.get_energy())
        animal.ate = True

    def infect(self, animal: Animal, food: Food):
        virus = food.virus[0]
        virus.phase = SYMBIOSIS
        animal.virus.append(virus)
        match (virus.trait):
            case config.VISION:
                virus.trait_val = animal.vision
                animal.vision = max(animal.vision + virus.effect, 0)
            case config.HIT:
               virus.trait_val = animal.hit
               animal.hit = max(animal.hit + virus.effect, 0)
            case config.LIFE:
                virus.trait_val = animal.life
                animal.life = max(animal.life + virus.effect, 0)
            case config.THRESHOLD:
               virus.trait_val = animal.threshold
               animal.threshold = max(animal.threshold + virus.effect, 0)

        food.virus = []


