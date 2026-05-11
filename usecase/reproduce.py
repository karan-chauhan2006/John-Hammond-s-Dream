import random
from ..Entities.world import World
from ..Entities.intent import Intent
from ..Entities.animal import Animal
from ..Entities.food import Food
from ..Entities.genealogy import Genealogy
from ..Entities.genealogy_data import GenealogyData
from ..config import MUTATION_CHOICE
from .config import REPRODUCE, TRAITS
from ..Entities.randomizer import Randomizer
from. import config
import math
class ReproduceUseCase:
    mutate_list: list #HLTV
    randomizer: Randomizer
    def  __init__(self, mutate_list: list, randomizer: Randomizer):
        self.mutate_list = mutate_list
        self.randomizer = randomizer

    def execute(self, world: World, genealogy: Genealogy):
        animals = world.get_animal_list()
        for key in list(animals.keys()):
            intent = world.get_animal(key).get_intent()
            if intent.get_kind() == REPRODUCE and not world.has_animal(intent.get_target()):
                parent = world.get_animal(key)
                child = self.create_child(parent, genealogy)
                self.update_parent(parent)
                if self.validate_child(child):
                    world.add_animal(child.get_pos(), child)
                    self.update_genes(child, parent, genealogy, world.get_state().turn)
                else:
                    type = self.randomizer.virus_randomiser.choice(TRAITS)
                    food = Food(child.get_energy(), child.get_pos(), type)
                    world.add_food(food.get_pos(), food)

    def update_genes(self, child: Animal, parent: Animal, geneaology: Genealogy, turn: int):
        data = GenealogyData(Id=child.Id, P_Id= parent.Id, lineage=child.lineage, gen=child.gen, birth_turn= turn,
                             birth_pos=child.pos, hit=child.hit, life=child.max_life,
                             b_threshold=child.min_threshold, vision=child.vision)
        geneaology.add_genealogy(data=data)

    def create_child(self, parent: Animal, genealogy: Genealogy) -> Animal:
        id = genealogy.max_id + 1
        hit_choice = self.randomizer.base_randomizer.choice(MUTATION_CHOICE)*self.mutate_list[0]
        ml_choice = self.randomizer.base_randomizer.choice(MUTATION_CHOICE)*self.mutate_list[1]
        threshold_choice = self.randomizer.base_randomizer.choice(MUTATION_CHOICE)*self.mutate_list[2]
        vision_choice = self.randomizer.base_randomizer.choice(MUTATION_CHOICE)*self.mutate_list[3]
        hit = parent.get_hit() + hit_choice
        max_life = parent.get_max_life() + ml_choice
        threshold = parent.get_threshold() + threshold_choice
        vision = parent.get_vision() + vision_choice
        gen = parent.get_gen() + 1
        pos = parent.get_intent().get_target()
        child = Animal(hit, max_life, threshold, vision, gen, pos, lineage= parent.get_lineage(), id= id)
        child.set_cooldown_attack(2)
        child.set_cooldown_aging(1)
        child.set_energy(parent.get_energy()/4)
        child.set_birthed(True)
        child.set_birth_pos(parent.get_pos())
        child.virus = parent.virus
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