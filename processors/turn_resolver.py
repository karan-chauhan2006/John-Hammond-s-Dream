from ..Entities.world import World
from ..Entities.genealogy import Genealogy
from ..usecase.food_decay import FoodDecayUseCase
from ..usecase.decide_intents import DecideIntentUseCase
from ..usecase.resolve_movement import ResolveMovementUseCase
from ..usecase.eating import EatUseCase
from ..usecase.aging import AgeUseCase
from ..usecase.death import DeathUseCase
from ..usecase.attack import ResolveAttackUseCase
from ..usecase.reproduce import ReproduceUseCase
from .state_updater import StateUpdater
from ..usecase.food_regen import FoodRegenUseCase
import random
class TurnResolver: 
    decide_intent: DecideIntentUseCase
    food_decay: FoodDecayUseCase
    resolve_movement: ResolveMovementUseCase
    eat: EatUseCase
    age: AgeUseCase
    death: DeathUseCase
    attack: ResolveAttackUseCase
    reproduce: ReproduceUseCase
    stateUpdater: StateUpdater
    food_regen: FoodRegenUseCase



    def __init__(self, mutate_list: list, eng_range: list, randomizer: random.Random):
        self.food_decay = FoodDecayUseCase()
        self.decide_intent = DecideIntentUseCase(randomizer)
        self.resolve_movement = ResolveMovementUseCase()
        self.eat = EatUseCase()
        self.age = AgeUseCase()
        self.death = DeathUseCase()
        self.attack = ResolveAttackUseCase()
        self.reproduce = ReproduceUseCase(mutate_list, randomizer)
        self.stateUpdater = StateUpdater()
        self.food_regen = FoodRegenUseCase(eng_range, randomizer)

    def step(self, world: World, genealogy: Genealogy) -> None:
        self.decide_intent.execute(world, genealogy)
        self.food_decay.execute(world)
        self.attack.execute(world)
        self.reproduce.execute(world, genealogy)
        self.resolve_movement.execute(world)
        self.eat.execute(world)
        self.age.execute(world)
        self.death.execute(world, genealogy)
        self.food_regen.execute(world)
        self.stateUpdater.execute(world)
        self.food_regen.caculate(world)
        
