from ..Entities.animal import Animal
from ..Entities.position import Position
from ..Entities.world import World
from ..Entities.intent import Intent
from .config import ATTACK
class ResolveAttackUseCase:

    def execute(self, world: World):
        animals = world.get_animal_list()
        damage: dict[Position, int] = {}
        for key in list(animals.keys()):
            if world.get_animal(key).get_intent().get_kind() == ATTACK:
                animal = world.get_animal(key)
                if animal.get_cooldown_attack() > 0: 
                    continue
                neighbours = world.neighbours(key)
                for pos in neighbours:
                    if world.has_animal(pos) and pos != key:
                        damage[pos] = damage.get(pos, 0) + animal.get_hit()
        for pos in list(damage.keys()):
            target = world.get_animal(pos)
            target.set_life(target.get_life()-damage[pos])
        world.get_state().set_total_combat(sum(damage.values()))



                        
