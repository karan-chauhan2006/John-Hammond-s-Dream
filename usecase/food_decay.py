from ..Entities.food import Food
from ..core.world import World
class FoodDecayUseCase: 

    def execute(self, world: World):
        foods = world.get_food_list()
        for key in list(foods.keys()):
            result = self.decay(foods[key])
            if not result:
                world.remove_food(key)

    def decay(self, food: Food) -> bool:
        if food.get_energy() > 1:
            food.set_energy(food.get_energy() -1)
            return True
        else:
            return False