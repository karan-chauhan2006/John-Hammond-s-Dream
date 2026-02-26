from .Entities.world import World
from .core.turn_resolver import Turn_Resolver
from .core.spawner import Spawner
from .core.runner import Runner
from .graphics.vizconfig import VizConfig
def main():
    W, H = 40,40
    turns = 300

    # Seed makes runs reproducible; change/remove if you want true randomness.
    world = World(W, H, seed=None)
    resolver = Turn_Resolver()
    spawner = Spawner(animal_units=100, food_units=1100, 
                      life_range=[1,20], hit_range=[1,5],
                       energy_range= [1,100], vision_range=[10,17],
                        max_turns=turns )
    world = spawner.fill(world)
    viz = Runner(W, H, VizConfig(cell_size=18, fps=30, autoplay_steps_per_sec=1))
    viz.run(world, resolver, max_turns=turns)
    
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
