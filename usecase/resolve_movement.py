from ..Entities.animal import Animal
from ..Entities.position import Position
from ..Entities.world import World
from ..Entities.intent import Intent
class ResolveMovementUseCase:

    def resolve_movement(self, animal: Animal, target: Position): 
        animal.set_pos(target)

    def execute(self, world: World):
        animals = world.get_animal_list()
        for key in list(animals.keys()):
            if world.get_animal(key).get_intent().get_kind() == "MOVE":
                animal = world.get_animal(key)
                target = world.get_animal(key).get_intent().get_target()
                if world.has_animal(target):
                    continue
                else:
                    self.resolve_movement(animal, target)
                    world.add_animal(target, animal)
                    world.remove_animal(key)
