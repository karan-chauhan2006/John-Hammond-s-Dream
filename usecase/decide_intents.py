import random
from ..Entities.intent import Intent
from ..Entities.animal import Animal
from ..Entities.position import Position
from ..Entities.world import World
from ..Entities.genealogy import Genealogy
from ..config import VERSION
from ..helpers.checker import check_threat
from . import config
import math
from ..Entities.mood import Mood
class DecideIntentUseCase:
    randomizer: random.Random
    checker: check_threat
    strat_change: bool

    def __init__(self, randomizer: random.Random):
        self.randomizer = randomizer
        self.checker = check_threat()
        self.strat_change = False

    def execute(self, world: World, genealogy: Genealogy):
        animals = world.get_animal_list()
        for key, animal in list(animals.items()):
            neighbours = world.neighbours(key)
            if self.checker.check(world,key,animal, genealogy, neighbours, VERSION):
                animal.set_intent(Intent(config.ATTACK, key))
            elif self.check_reproduce(world, animal):
                animal.set_intent(Intent(config.REPRODUCE, self.choose_birth(world, animal)))
            else:
                data = self.scan(animal, world, genealogy) 
                self.resolve_strat(data, animal)
                self.resolve_mood(data, animal, world, genealogy)
                self.resolve_intent(animal, world, genealogy)

    def resolve_intent(self, animal: Animal, world: World, genealogy: Genealogy):
        char = animal.mood.type
        match(char):
            case 'E'  :
                pos = self.choose_direction(world, animal.pos, animal.mood.target.pos)
                animal.intent = Intent(config.MOVE, pos)
            case 'T' | 'F':
                pos = self.choose_direction_diagonal(world, animal.pos, animal.mood.target.pos)
                animal.intent = Intent(config.MOVE, pos)
            case 'M' | 'B' | 'A':
                pos = self.choose_direction(world, animal.pos, animal.mood.target)
                animal.intent = Intent(config.MOVE, animal.mood.target)
    
    def resolve_mood(self, data: dict, animal: Animal, world: World, genealogy: Genealogy):
       check = self.check_mood(animal, world, genealogy)
       if check:
            char = animal.strategy[0]
            if len(animal.strategy) > 1:
                animal.strategy = animal.strategy[1:]
            else:
                animal.strategy = None
            if self.strat_change:
                start = animal.pos
                self.strat_change = False
            else:
                start = animal.mood.start
            match(char):
                case 'E':
                    animal.mood = Mood(char,data["near_food"],start)
                case 'M':
                    pos = animal.pos
                    animal.mood = Mood(char,Position(pos.get_x()+animal.vision, pos.get_y() + animal.vision),start)
                case 'B':
                    animal.mood = Mood(char,start,start)
                case 'T' | 'F':
                    animal.mood = Mood(char,data["near_animal"],start)
                case 'A':
                    pos = self.randomizer.choice(world.neighbours(animal.pos))
                    animal.mood = Mood(char,pos,start)

       else:
           return

    def check_mood(self, animal: Animal, world: World, genealogy: Genealogy):
        if animal.mood is None:
            return True
        match(animal.mood.type):
            case 'E':
                return not world.has_food(animal.mood.target.pos)
            case 'M' | 'B' | 'A':
                return world.distance(animal.pos, animal.mood.target) == 0
            case 'T' | 'F':
                distance = world.distance(animal.pos, animal.mood.target.pos)
                return distance > animal.vision or not genealogy.is_alive(animal.mood.target.Id)

    def resolve_strat(self, data: dict, animal: Animal):
        if animal.strategy is None:
            context_data = self.cotext(data, animal)
            knowledge = animal.knowledge
            m_val = 0
            strat = ""
            for obj in list(knowledge.keys()):
                sum = 0
                chars = list(set(obj))
                length = len(obj)
                for char in chars:
                    count = obj.count(char)
                    match(char):
                        case 'E':
                            sum += count * context_data["f_factor"] / length
                        case 'M' | 'B' | 'A':
                            sum += count * context_data["s_factor"] / length
                        case 'T' | 'F':
                            sum += count * context_data["a_factor"] / length
                sum = knowledge[obj] * sum
                if sum > m_val:
                    strat = obj
            if strat == "":
                strat = self.randomizer.choice(list(knowledge.keys()))
            animal.strategy = strat
            self.strat_change = True
        else:
            self.strat_change = False
    

                        



    def cotext(self, data, animal: Animal) -> dict:
        vision = animal.vision
        total = 2* (vision  + 1) * vision
        a_factor = data["animal_num"]/ total
        f_factor = data["food_num"]/total
        s_factor = 1 - a_factor - f_factor
        return {
            "a_factor": a_factor,
            "f_factor": f_factor,
            "s_factor": s_factor,
            "near_animal": data["near_animal"],
            "near_food": data["near_food"]
        }

            
    def scan(self, animal: Animal, world: World, genealogy: Genealogy) -> dict:
        a_count = 0
        f_count = 0
        n_food = None
        n_animal = None
        m_a_dis = animal.vision+1
        m_f_dis = animal.vision+1
        for dx in range(math.floor(-animal.vision), math.floor(animal.vision + 1)):
            y_range = math.floor(animal.vision)-abs(dx)
            for dy in range(-y_range, y_range+1):
                pos = Position(animal.pos.get_x() + dx, animal.pos.get_y()+dy)
                if world.has_animal(pos):
                    a_count += 1
                    dis = world.distance(animal.pos, pos)
                    if dis < m_a_dis:
                        n_animal = world.get_animal(pos)
                        m_a_dis = dis

                elif world.has_food(pos):
                    f_count += 1
                    dis = world.distance(animal.pos, pos)
                    if dis < m_f_dis:
                        n_food = world.get_food(pos)
                        m_f_dis = dis
                else:
                    continue
        if a_count == 0:
            n_animal = animal
        if f_count == 0:
            n_food = animal
        return {
            "animal_num": a_count,
            "food_num": f_count,
            "near_animal":  n_animal,
            "near_food": n_food
        }
    
    # def execute(self, world: World, genealogy: Genealogy):
    #     #main executer and sets intent
    #     animals = world.get_animal_list()
    #     for key,animal in list(animals.items()):
    #         neighbours = world.neighbours(key)
    #         if self.checker.check(world, key, animal, genealogy, neighbours, VERSION):
    #            animal.set_intent(Intent(config.ATTACK, key))
    #         elif self.check_reproduce(world, key, neighbours):
    #             animal.set_intent(Intent(config.REPRODUCE, self.choose_birth(world, key, neighbours)))
    #         else: 
    #             animal.set_intent( Intent(config.MOVE, self.choose_direction(world, key)))
    #         animal.set_birthed(False)

    
    
        

    
    def choose_direction(self, world: World, pos: Position, loc: Position) -> Position:
        # chooses which direction to move in 
        if loc == pos:
            return pos
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
                return self.randomizer.choice(final)

    def choose_direction_diagonal(self, world: World, pos: Position, loc: Position) -> Position:
        # chooses which direction to move in 
        dx = loc.get_x() - pos.get_x()
        dy = loc.get_y() - pos.get_y()

        if dx == 0 and dy == 0:
            return pos

        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)

        return Position(pos.get_x() + step_x, pos.get_y() + step_y)
           
            



        

    # def find_loc(self, world: World, pos: Position) -> Position:
    #     # finds the direction of the closes food
    #     flag = False
    #     vision = world.get_animal(pos).get_vision()
    #     min_dis = world.W + world.H + 10
    #     min_pos = Position(0,0)
    #     for dx in range(-math.floor(vision), math.floor(vision)+1):
    #         max_dy = math.floor(vision) - abs(dx)
    #         for dy in range(-max_dy, max_dy + 1):
    #             loc = Position(pos.x+dx, pos.y+dy)
    #             if world.has_food(loc):
    #                 if world.distance(pos,loc) < min_dis:
    #                     min_pos = loc
    #                     min_dis = world.distance(pos,loc)
    #                     flag = True

    #     if flag:
    #         return min_pos
    #     else:
    #         return pos
        
    def check_reproduce(self, world: World, animal: Animal) -> bool: 
        # checks if the animal can reproduce
        flag = True
        neighbours = world.neighbours(animal.pos)
        if animal.get_energy() < animal.get_threshold():
            flag = False
        

        count = 4
        for n in neighbours:
            if not(world.is_empty(n)):
                count -= 1
        
        if count == 0:
            flag = False

        return flag

    def choose_birth(self, world: World, animal: Animal) -> Position:
        # chooses teh location to reproduce
        empty = []
        neighbours = world.neighbours(animal.pos)
        for n in neighbours:
            if world.is_empty(n):
                empty.append(n)
        return self.randomizer.choice(empty)
                    