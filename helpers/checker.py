from ..Entities.world import World
from ..Entities.position import Position
from ..Entities.animal import Animal
from ..Entities.genealogy import Genealogy
from . import config
class check_threat:

    def check(self ,world: World, pos: Position, animal: Animal, 
                     genealogy: Genealogy, neighbours: list[Position], version: str) -> bool:
         # checks if the animal is under attack
        for loc in neighbours:
            if loc!= pos and world.has_animal(loc):
                if animal.get_birthed() and loc == animal.get_birth_pos():
                    continue
                elif self.check_gen(world, loc, animal, genealogy, version):
                    continue
                else:
                    return True
        return False

    def check_gen(self, world: World, loc: Position, animal: Animal, genealogy: Genealogy, Version: str) -> bool:
            # chooses which version of attack the run is working with and checks that
            match(Version):
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