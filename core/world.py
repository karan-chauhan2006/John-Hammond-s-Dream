import random
from typing import Optional
from .position import Position
from ..Entities.animal import Animal
from ..Entities.food import Food
class World: 
    W: int
    H: int
    animals: dict[Position, Animal]
    foods: dict[Position, Food]

    def __init__(self, W: int, H: int, seed: Optional[int] = None):
        self.W = W
        self.H = H
        self.rng = random.Random(seed)
        self.animals = {}
        self.foods = {}

    def wrap(self, pos: Position) -> Position:
        return Position(pos.x % self.W, pos.y % self.H)
    
    def neighbours(self, pos: Position) -> list[Position]:
        lst = pos.neighbours()
        result = []
        for loc in lst:
            result.append(self.wrap(loc))
        return result
    
    def neighbours_x(self, pos: Position) -> list[Position]:
        lst = pos.neighbours_x()
        result = []
        for loc in lst:
            result.append(self.wrap(loc))
        return result
    
    def neighbours_y(self, pos: Position) -> list[Position]:
        lst = pos.neighbours_y()
        result = []
        for loc in lst:
            result.append(self.wrap(loc))
        return result
    

    def distance(self, pos_a: Position, pos_b: Position) -> int:
        dx = abs(pos_a.get_x() - pos_b.get_x())
        dy = abs(pos_a.get_y() - pos_b.get_y())
        dx = min(dx, self.W - dx)
        dy = min(dy, self.H - dy)
        return dx+dy
    
    def distance_x(self, pos_a: Position, pos_b: Position) -> int:
        dx = abs(pos_a.get_x() - pos_b.get_x())
        dx = min(dx, self.W - dx)
        return dx

    def distance_y(self, pos_a: Position, pos_b: Position) -> int:
        dy = abs(pos_a.get_y() - pos_b.get_y())
        dy = min(dy, self.H - dy)
        return dy   

    def is_empty(self, pos: Position) -> bool: 
        return not (self.has_animal(pos) or self.has_food(pos)) 
    


    def has_animal(self, pos: Position) -> bool:
        return pos in self.animals
    
    def has_food(self, pos: Position) -> bool:
        return pos in self.foods
    
    def get_animal_list(self) -> dict[Position, Animal]:
        return self.animals
    
    def get_animal(self, pos: Position) -> Animal: 
        return self.animals[pos]
    
    def get_food_list(self) -> dict[Position, Food]:
        return self.foods
    
    def get_food(self, pos: Position) -> bool: 
        return self.foods[pos]
    
    def add_animal(self, pos: Position, animal: Animal):
        self.animals[pos] = animal

    def add_food(self, pos: Position, food: Food):
        self.foods[pos] = food

    def move_animal(self, from_pos: Position, to_pos: Position) -> None:
        if from_pos not in self.animals:
            raise KeyError(from_pos)
        if self.has_animal(to_pos):
            return  
        animal = self.animals.pop(from_pos)
        animal.x, animal.y = to_pos
        self.animals[to_pos] = animal
    
    def remove_animal(self, pos: Position) -> None:
        self.animals.pop(pos, None)

    def remove_food(self, pos: Position) -> None:
        self.foods.pop(pos, None)

    def random_cell(self) -> Position:
        return Position(self.rng.randrange(self.W), self.rng.randrange(self.H))

    def random_empty_cell(self) -> Position:
        for _ in range(self.W * self.H * 3):
            pos = self.random_cell()
            if not self.has_animal(pos) and not self.has_food(pos):
                return pos
        raise RuntimeError("Could not find empty cell for animal (world too full?)")

    
