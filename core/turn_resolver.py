from ..Entities.world import World
from ..usecase.food_decay import FoodDecayUseCase
from ..usecase.decide_intents import DecideIntentUseCase
from ..usecase.resolve_movement import ResolveMovementUseCase
from ..usecase.eating import EatUseCase
from ..usecase.aging import AgeUseCase
from ..usecase.death import DeathUseCase
from ..usecase.attack import ResolveAttackUseCase
from ..usecase.reproduce import ReproduceUseCase
from .state_updater import StateUpdater
class Turn_Resolver: 
    decide_intent: DecideIntentUseCase
    food_decay: FoodDecayUseCase
    resolve_movement: ResolveMovementUseCase
    eat: EatUseCase
    age: AgeUseCase
    death: DeathUseCase
    attack: ResolveAttackUseCase
    reproduce: ReproduceUseCase
    stateUpdater: StateUpdater



    def __init__(self):
        self.food_decay = FoodDecayUseCase()
        self.decide_intent = DecideIntentUseCase()
        self.resolve_movement = ResolveMovementUseCase()
        self.eat = EatUseCase()
        self.age = AgeUseCase()
        self.death = DeathUseCase()
        self.attack = ResolveAttackUseCase()
        self.reproduce = ReproduceUseCase()
        self.stateUpdater = StateUpdater()

    def step(self, world: World) -> None:
        self.decide_intent.execute(world)
        self.food_decay.execute(world)
        self.attack.execute(world)
        self.reproduce.execute(world)
        self.resolve_movement.execute(world)
        self.eat.execute(world)
        self.age.execute(world)
        self.death.execute(world)
        self.stateUpdater.execute(world)
        
