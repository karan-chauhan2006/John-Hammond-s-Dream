import random
from ..Entities.world import World
from ..Entities.intent import Intent
from ..Entities.animal import Animal
from ..Entities.food import Food
class ReproduceUseCase:
    def execute(self, world: World):
        animals = world.get_animal_list()
        for key in list(animals.keys()):
            if world.get_animal(key).get_intent().get_kind() == "REPRODUCE":
                parent = world.get_animal(key)
                child = self.create_child(parent)
                self.update_parent(parent)
                if self.validate_child(child):
                    world.add_animal(child.get_pos(), child)
                else:
                    food = Food(child.get_energy(), child.get_pos())
                    world.add_food(food.get_pos(), food)


    def create_child(self, parent: Animal) -> Animal:
        hit = parent.get_hit() + random.choice([-1,0,1])
        max_life = parent.get_max_life() + random.choice([-1,0,1])
        threshold = parent.get_threshold() + random.choice([-1,0,1])
        vision = parent.get_vision() + random.choice([-1,0,1])
        gen = parent.get_gen() + 1
        pos = parent.get_intent().get_target()
        child = Animal(hit, max_life, threshold, vision, gen, pos, lineage= parent.get_lineage())
        child.set_cooldown_attack(2)
        child.set_cooldown_aging(1)
        child.set_energy(parent.get_energy()/4)
        child.set_birthed(True)
        child.set_birth_pos(parent.get_pos())
        return child
        
    def update_parent(self, parent: Animal):
        parent.set_cooldown_aging(2)
        parent.set_cooldown_attack(2)
        parent.set_energy(parent.get_energy()/2)
        parent.set_birthed(True)
        parent.set_birth_pos(parent.get_intent().get_target())

    def validate_child(self, child: Animal) -> bool:
        flag = True
        if child.get_max_life() <= 0:
            flag = False
        
        if child.get_threshold() <= 0:
            flag = False

        if child.get_hit() < 0:
            flag = False

        if child.get_vision() < 0:
            flag = False
        return flag