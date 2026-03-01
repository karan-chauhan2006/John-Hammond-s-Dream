from .Entities.world import World
from .Entities.spawn_data import SpawnData
from .processors.turn_resolver import Turn_Resolver
from .processors.spawner import Spawner
from .processors.runner import Runner
from .graphics.vizconfig import VizConfig
from .data_processors.data_plotter import DataPlotter
def main():
    W, H = 40,40
    turns = 1000

    # Seed makes runs reproducible; change/remove if you want true randomness.
    world = World(W, H, seed=10)
    spawn_data = SpawnData(animal_units=100, food_units=600, 
                      life_range=[1,50], hit_range=[1,10],
                       energy_range= [1,100], vision_range=[10,15],
                        max_turns=turns)
    resolver = Turn_Resolver(spawn_data.get_mutate_list(), spawn_data.get_eng_list())
    spawner = Spawner(spawn_data)
    world = spawner.fill(world)
    viz = Runner(W, H, VizConfig(cell_size=18, fps=30, autoplay_steps_per_sec=1))
    handler = viz.run(world, resolver, max_turns=turns)
    path = handler.save_data(spawn_data.get_data(W,H))
    DataPlotter(path).plot()
    
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
