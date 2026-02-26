from ..Entities.world import World
from ..Entities.animal import Animal
from ..Entities.food import Food
class EatUseCase:

    def execute(self, world: World):
        foods = world.get_food_list()
        for key in list(foods.keys()):
            if world.has_animal(key):
                animal = world.get_animal(key)
                food = world.get_food(key)
                self.eat(animal, food)
                world.remove_food(key)
            else:
                continue
        
    def eat(self, animal: Animal, food: Food):
        energy = animal.get_energy()
        animal.set_energy(energy + food.get_energy())
