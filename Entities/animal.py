from .position import Position
from .intent import Intent
from .mood import Mood
from ..config import REPRODUCTION_CONSTANT, LIFE_DIVIDER
from bidict import bidict

import math
class Animal:
    #traits
    hit: float
    max_life: float
    min_threshold: float
    vision: float
    gen: int = 0
    lineage: int = None
    Id: int 
    

    #mutables
    knowledge: dict
    strategy: str
    mood: Mood
    intent: Intent
    cooldown_attack: int = 0
    cooldown_aging: int = 0
    pos: Position
    energy: float
    threshold: float

    #constants & intenral logic
    birthed: bool = False
    child_birth_pos: Position = Position(None, None)
    life_divider: int
    divide_counter: int = 0
    threshold_buffer: int = 0
    ate: bool = False
    life: float

    
    def __init__(self, hit: int, max_life: int, threshold: float,
                  vision: int, gen: int, pos: Position, lineage: int, id: int,
                  knowledge: bidict):
        self.hit = hit
        self.max_life = max_life
        self.life = max_life
        self.threshold = threshold
        self.min_threshold = threshold
        self.energy = threshold/REPRODUCTION_CONSTANT
        self.vision = vision
        self.gen = gen
        self.pos = pos
        self.knowledge = knowledge
        self.strategy = None
        self.mood = None 
        self.intent = Intent(None, None)
        self.lineage = lineage
        self.life_divider = LIFE_DIVIDER
        self.threshold_buffer = math.ceil(threshold/(self.life_divider))
        self.ate = False
        self.Id = id
        pass 


    def get_lineage(self) -> int:
        return self.lineage

    def get_energy(self) -> float:
        return self.energy

    def get_pos(self) -> Position:
        return self.pos
    
    def get_hit(self) -> float:
        return self.hit
    
    def get_threshold(self) -> float:
        return self.threshold
    
    def get_vision(self) -> int:
        return self.vision
    
    def get_gen(self) -> int:
        return self.gen
    
    def get_cooldown_attack(self) -> int:
        return self.cooldown_attack
    
    def get_cooldown_aging(self) -> int:
        return self.cooldown_aging
    
    def get_max_life(self) -> int:
        return self.max_life
    
    def get_life(self) -> int:
        return self.life
    
    def get_intent(self) -> Intent:
        return self.intent
    
    def get_birthed(self) -> bool: 
        return self.birthed
    
    def get_birth_pos(self) -> Position:
        return self.child_birth_pos
    

    def set_energy(self, energy: float):
        self.energy = energy

    def set_pos(self, pos: Position):
        self.pos = pos

    def set_hit(self, hit: int):
        self.hit = hit
    
    def set_max_life(self, max_life: int):
        self.max_life = max_life

    def set_life(self, life: int):
        self.life = life

    def set_threshold(self, threshold: float):
        self.threshold = threshold

    def set_vision(self, vision: int):
        self.vision = vision

    def set_gen(self, gen: int):
        self.gen = gen

    def set_cooldown_attack(self, cooldown_atack: int):
        self.cooldown_attack = cooldown_atack

    def set_cooldown_aging(self, cooldown_aging: float):
        self.cooldown_aging = cooldown_aging
    
    def set_intent(self, intent: Intent):
        self.intent = intent

    def set_birthed(self, birthed: bool):
        self.birthed = birthed

    def set_birth_pos(self, pos: Position):
        self.child_birth_pos = pos

    def set_lineage(self, lin: int):
        self.lineage = lin