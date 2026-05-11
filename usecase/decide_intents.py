import random
from ..Entities.intent import Intent
from ..Entities.animal import Animal
from ..Entities.position import Position
from ..Entities.world import World
from ..Entities.genealogy import Genealogy
from ..config import VERSION
from . import config
import math
from ..Entities.randomizer import Randomizer
class DecideIntentUseCase:
    randomizer: Randomizer

    def __init__(self, randomizer: Randomizer):
        self.randomizer = randomizer
        
    
    def execute(self, world: World, genealogy: Genealogy):
        #main executer and sets intent
        animals = world.get_animal_list()
        for key,animal in list(animals.items()):
            neighbours = world.neighbours(key)
            if self.check_attack(world, key, animal, genealogy, neighbours):
               animal.set_intent(Intent(config.ATTACK, key))
            elif self.check_reproduce(world, key, neighbours):
                animal.set_intent(Intent(config.REPRODUCE, self.choose_birth(world, key, neighbours)))
            else: 
                animal.set_intent( Intent(config.MOVE, self.choose_direction(world, key)))
            animal.set_birthed(False)
    
    def check_attack(self ,world: World, pos: Position, animal: Animal, 
                     genealogy: Genealogy, neighbours: list[Position]) -> bool:
        # checks if the animal is under attack
        for loc in neighbours:
            if loc!= pos and world.has_animal(loc):
                if animal.get_birthed() and loc == animal.get_birth_pos():
                    continue
                elif self.check_gen(world, loc, animal, genealogy):
                    continue
                else:
                    return True
        return False
    
    def check_gen(self, world: World, loc: Position, animal: Animal, genealogy: Genealogy) -> bool:
        # chooses which version of attack the run is working with and checks that
        match(VERSION):
            case config.V1:
                return self.check_genv1(world, loc, animal)
            case config.V2:
                return self.check_genv2(world, loc, animal)
            case config.V3:
                return self.check_genv3(world, loc, animal)
            case config.V4:
                return self.check_genv4(world, loc, animal)
            case config.V5:
                return self.check_genv5(world,loc,animal,genealogy)
    
    def check_genv1(self, world: World, pos: Position, animal: Animal) -> bool:
        #same lineage gen +- 1
        posGen = [animal.get_gen()-1, animal.get_gen(), animal.get_gen()+1]
        if animal.get_lineage() != world.get_animal(pos).get_lineage():
            return False
        if not posGen.__contains__(world.get_animal(pos).get_gen()):
            return False
        return True
    
    def check_genv2(self, world: World, pos: Position, animal: Animal):
        # same lineage
        if animal.get_lineage() != world.get_animal(pos).get_lineage():
            return False
        return True

    def check_genv3(self, world: World, pos: Position, animal: Animal):
        #none 
        return False

    def check_genv4(self, world: World, pos: Position, animal: Animal):
        #gen+-1
        posGen = [animal.get_gen()-1, animal.get_gen(), animal.get_gen()+1]
        if not posGen.__contains__(world.get_animal(pos).get_gen()):
            return False
        return True

    def check_genv5(self, world: World,pos: Position,animal: Animal,genealogy: Genealogy):
        attacker_lookup = genealogy.lookup(animal.Id)
        defender_lookup = genealogy.lookup(world.get_animal(pos).Id)
        return not (attacker_lookup == defender_lookup)
        #common uniter
        

    
    def choose_direction(self, world: World, pos: Position) -> Position:
        # chooses which direction to move in 
        loc = self.find_loc(world,pos)
        if loc == pos:
            return self.randomizer.base_randomizer.choice(world.neighbours(pos))
        else:
            min_dis = world.distance(pos, loc)
            dis_x = world.distance_x(pos, loc)
            dis_y = world.distance_y(pos, loc)
            candid = []
            if dis_x > dis_y:
                candid = world.neighbours_x(pos)
            elif dis_x < dis_y:
                candid = world.neighbours_y(pos)
            else: 
                candid = world.neighbours(pos)
            final = []
            for d in candid: 
                if world.distance(d,loc) < min_dis:
                    final.append(d)
            animal = world.get_animal(pos)
            if animal.get_birthed() and final.__contains__(animal.get_birth_pos()):
                final.remove(world.get_animal(pos).get_birth_pos())
            if len(final) == 0:
                return pos
            else:
                return self.randomizer.base_randomizer.choice(final)


        

    def find_loc(self, world: World, pos: Position) -> Position:
        # finds the direction of the closes food
        flag = False
        vision = world.get_animal(pos).get_vision()
        min_dis = world.W + world.H + 10
        min_pos = Position(0,0)
        for dx in range(-math.floor(vision), math.floor(vision)+1):
            max_dy = math.floor(vision) - abs(dx)
            for dy in range(-max_dy, max_dy + 1):
                loc = Position(pos.x+dx, pos.y+dy)
                if world.has_food(loc):
                    if world.distance(pos,loc) < min_dis:
                        min_pos = loc
                        min_dis = world.distance(pos,loc)
                        flag = True

        if flag:
            return min_pos
        else:
            return pos
        
    def check_reproduce(self, world: World, pos: Position, neighbours: list[Position]) -> bool: 
        # checks if the animal can reproduce
        animal = world.get_animal(pos)
        flag = True
        if animal.get_energy() < animal.get_threshold():
            flag = False
        

        count = 4
        for n in neighbours:
            if not(world.is_empty(n)):
                count -= 1
        
        if count == 0:
            flag = False

        return flag

    def choose_birth(self, world: World, pos: Position, neighbours: list[Position]) -> Position:
        # chooses teh location to reproduce
        empty = []
        for n in neighbours:
            if world.is_empty(n):
                empty.append(n)
        return self.randomizer.base_randomizer.choice(empty)
                    