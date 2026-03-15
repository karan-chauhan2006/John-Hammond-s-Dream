from ..Entities.world import World
from ..Entities.genealogy import Genealogy
class FlushUseCase: 
    def execute(self, world: World, genealogy: Genealogy): 
        animal_list = world.get_animal_list()
        turn = world.get_state().turn
        for animal in list(animal_list.values()):
            id = animal.Id
            pos = animal.pos
            threshold = animal.threshold
            genealogy.finalise_genealogy(id, turn, pos, threshold)