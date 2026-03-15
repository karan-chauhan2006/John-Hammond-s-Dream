from .Entities.world import World
from .Entities.spawn_data import SpawnData
from .processors.turn_resolver import TurnResolver
from .processors.spawner import Spawner
from .processors.runner import Runner
from .graphics.vizconfig import VizConfig
from .data_processors.data_plotter import DataPlotter
import random
from .config import W, H, TURNS, SEED, ANIMAL_UNITS, FOOD_UNITS, TAU
from .config import LIFE_RANGE, HIT_RANGE, ENERGY_RANGE, VISION_RANGE
from datetime import datetime
from .data_processors.data_handler import DataHandler
from .Entities.genealogy import Genealogy
def main():
    now = datetime.now()
    time = now.strftime("%Y_%m_%d_%H_%M_%S")
    name = f"{time}_{SEED}"
    randomizer = random.Random(SEED)
    handler = DataHandler(name)
    handler.start()
    # Seed makes runs reproducible; change/remove if you want true randomness.
    world = World(W, H, randomizer)
    genealogy = Genealogy()
    spawn_data = SpawnData(animal_units=ANIMAL_UNITS, food_units=FOOD_UNITS, 
                      life_range=LIFE_RANGE, hit_range=HIT_RANGE,
                       energy_range= ENERGY_RANGE, vision_range=VISION_RANGE,
                        max_turns=TURNS)
    handler.record_spawn_data(spawn_data.get_data())
    resolver = TurnResolver(spawn_data.get_mutate_list(), spawn_data.get_eng_list(), randomizer)
    spawner = Spawner(spawn_data, randomizer)
    world, genealogy = spawner.fill(world, genealogy)
    viz = Runner(W, H, VizConfig(cell_size=18, fps=30, autoplay_steps_per_sec=1), handler)
    viz.run(world, genealogy, resolver, max_turns=TURNS)
    handler.close()
    DataPlotter(name, TAU).plot()
    
    # for t in range( turns + 1):
    #     if t!=0:
    #         resolver.step(world)

    #     animals_count = len(world.animals)
    #     foods_count = len(world.foods)

    #     if animals_count > 0:
    #         avg_energy = sum(a.energy for a in world.animals.values()) / animals_count
    #     else:
    #         avg_energy = 0.0

    #     print(
    #         f"Turn {t:03d} | "
    #         f"Animals: {animals_count:4d} | "
    #         f"Food: {foods_count:4d} | "
    #         f"Avg animal energy: {avg_energy:7.2f}"
    #     )

    #     # Optional early stop if extinct
    #     if animals_count == 0:
    #         print("All animals extinct. Stopping.")
    #         break

if __name__ == "__main__":
    main()
