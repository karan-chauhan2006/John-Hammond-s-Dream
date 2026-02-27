import random
from ..Entities.intent import Intent
from ..Entities.animal import Animal
from ..Entities.position import Position
from ..Entities.world import World

class DecideIntentUseCase:
    
    def execute(self, world: World):
        animals = world.get_animal_list()
        for key in list(animals.keys()):
            animal = world.get_animal(key)
            if self.check_attack(world, key, animal):
               animal.set_intent(Intent("ATTACK", key))
            elif self.check_reproduce(world, key):
                animal.set_intent(Intent("REPRODUCE", self.choose_birth(world, key)))
            else: 
                animal.set_intent( Intent("MOVE", self.choose_direction(world, key)))
            animal.set_birthed(False)
    
    def check_attack(self ,world: World, pos: Position, animal: Animal) -> bool:
        neighbours = world.neighbours(pos)
        for loc in neighbours:
            if loc!= pos and world.has_animal(loc):
                if world.get_animal(pos).get_birthed() and loc == world.get_animal(pos).get_birth_pos():
                    continue
                elif self.check_genv1(world, loc, animal):
                    continue
                else:
                    return True
        return False
    
    def check_genv1(self, world: World, pos: Position, animal: Animal) -> bool:
        #same lineage gen +- 1
        posGen = [animal.get_gen()-1, animal.get_gen(), animal.get_gen()+1]
        if animal.get_lineage() != world.get_animal(pos).get_lineage():
            return False
        if not posGen.__contains__(world.get_animal(pos).get_gen()):
            return False
        return True
    
    def check_genv2():
        # same lineage
        pass

    def check_genv3():
        #none 
        pass

    def check_genv4():
        #gen+-1
        pass

    def check_genv5():
        #common uniter
        pass

    
    def choose_direction(self, world: World, pos: Position) -> Position:
        loc = self.find_loc(world,pos)
        if loc == pos:
            return random.choice(world.neighbours(pos))
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
            if world.get_animal(pos).get_birthed() and final.__contains__(world.get_animal(pos).get_birth_pos()):
                final.remove(world.get_animal(pos).get_birth_pos())
            if len(final) == 0:
                return pos
            else:
                return random.choice(final)


        

    def find_loc(self, world: World, pos: Position) -> Position:
        flag = False
        vision = world.get_animal(pos).get_vision()
        min_dis = world.W + world.H + 10
        min_pos = Position(0,0)
        for loc in list(world.get_food_list().keys()):
            if world.distance(pos,loc) <= vision:
                if world.distance(pos,loc) < min_dis:
                    min_pos = loc
                    min_dis = world.distance(pos,loc)
                    flag = True
        if flag:
            return min_pos
        else:
            return pos
        
    def check_reproduce(self, world: World, pos: Position) -> bool: 
        animal = world.get_animal(pos)
        flag = True
        if animal.get_energy() < animal.get_threshold():
            flag = False
        
        neighbours = world.neighbours(pos)
        count = 4
        for n in neighbours:
            if not(world.is_empty(n)):
                count -= 1
        
        if count == 0:
            flag = False

        return flag

    def choose_birth(self, world: World, pos: Position) -> Position:
        neighbours = world.neighbours(pos)
        empty = []
        for n in neighbours:
            if world.is_empty(n):
                empty.append(n)
        return random.choice(empty)
                    