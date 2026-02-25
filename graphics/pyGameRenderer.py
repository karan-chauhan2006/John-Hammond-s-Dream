import pygame
import sys
from .vizconfig import VizConfig, clamp01, lerp, rgb
from ..core.world import World
from ..Entities.food import Food
from ..Entities.animal import Animal
class PygameRenderer:
    def __init__(self, W: int, H: int, cfg: VizConfig):
        pygame.init()
        self.W, self.H = W, H
        self.cfg = cfg
        self.width_px = W * cfg.cell_size
        self.height_px = H * cfg.cell_size

        self.screen = pygame.display.set_mode((self.width_px, self.height_px))
        pygame.display.set_caption("Ecosystem")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 16)

        self.turn = 0
        self.autoplay = False
        self.steps_per_sec = cfg.autoplay_steps_per_sec
        self._accum = 0.0  # time accumulator for stepping

    def handle_events(self):
        step_once = False
        restart = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

                if event.key == pygame.K_SPACE:
                    step_once = True

                if event.key == pygame.K_RETURN:
                    self.autoplay = not self.autoplay

                if event.key == pygame.K_UP:
                    self.steps_per_sec = min(200, self.steps_per_sec + 5)

                if event.key == pygame.K_DOWN:
                    self.steps_per_sec = max(1, self.steps_per_sec - 5)

                if event.key == pygame.K_r:
                    restart = True

        return step_once, restart

    def draw(self, world: World, combat_damage=None):
        cs = self.cfg.cell_size
        self.screen.fill((0, 0, 0))

        # --- Draw food first (so animals draw on top) ---
        for key in list(world.get_food_list().keys()):
            food: Food = world.get_food(key)
            e = food.get_energy()
            # map food energy -> green brightness
            g = clamp01(0.2 + 0.03 * e)
            color = rgb(0, 255 * g, 0)
            rect = pygame.Rect(food.get_pos().x * cs, food.get_pos().y * cs, cs, cs)
            pygame.draw.rect(self.screen, color, rect)

        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)
            energy = getattr(a, "energy", 0)
            life = getattr(a, "life", 1)
            max_life = getattr(a, "max_life", 1)
            cd = getattr(a, "cooldown_attack", 0)

            # Choose what you want to visualize:
            # 1) Energy view:
            t = clamp01(0.10 + 0.02 * energy)
            # 2) Life view (uncomment):
            # t = clamp01(life / max(1, max_life))

            # Color ramp: dark red -> bright orange/yellow-ish
            r = 255 * lerp(0.35, 1.0, t)
            g = 255 * lerp(0.05, 0.65, t)
            b = 0

            # If on attack cooldown, tint blue (so you can "see" cooldown waves)
            if cd > 0:
                b = min(200, 60 * cd)

            color = rgb(r, g, b)
            rect = pygame.Rect(a.get_pos().x * cs, a.get_pos().y * cs, cs, cs)
            pygame.draw.rect(self.screen, color, rect)

        # --- Optional grid lines ---
        if self.cfg.grid_lines and cs >= 10:
            line_color = (25, 25, 25)
            for x in range(self.W + 1):
                pygame.draw.line(self.screen, line_color, (x * cs, 0), (x * cs, self.height_px))
            for y in range(self.H + 1):
                pygame.draw.line(self.screen, line_color, (0, y * cs), (self.width_px, y * cs))

        # --- HUD text (top-left) ---
        hud = f"Turn {self.turn:04d} | A={len(world.animals)} F={len(world.foods)} | "
        hud += "AUTO" if self.autoplay else "PAUSE"
        hud += f" | {self.steps_per_sec} tps"
        if combat_damage is not None:
            hud += f" | dmg={combat_damage}"

        # Draw HUD with a slight shadow for readability
        surf1 = self.font.render(hud, True, (0, 0, 0))
        surf2 = self.font.render(hud, True, (220, 220, 220))
        self.screen.blit(surf1, (9, 9))
        self.screen.blit(surf2, (8, 8))

        pygame.display.flip()

    def run(self, world: World, resolver, max_turns=1000000):
        dt = 0.0
        self.turn = 0
        self.autoplay = False
        self._accum = 0.0
        world.print_state()

        while self.turn <= max_turns:
            self.clock.tick(self.cfg.fps)
            dt = self.clock.get_time() / 1000.0

            step_once, restart = self.handle_events()
            if restart or len(world.animals) == 0:
                # You implement: reset world+resolver state however you do it
                # world = World(self.W, self.H, seed=None)
                # spawner.spawn(world) ...
                # resolver = Turn_Resolver() ...
                self.autoplay = False

            # Autoplay stepping (fixed turns/sec)
            if self.autoplay:
                self._accum += dt
                step_interval = 1.0 / max(1, self.steps_per_sec)
                while self._accum >= step_interval:
                    self._accum -= step_interval
                    resolver.step(world)  # <- your turn advancement
                    self.turn += 1
                    world.print_state()
                    

            # Manual single-step
            if step_once:
                resolver.step(world)
                self.turn += 1
                world.print_state()

            # If you have combat damage stored, pass it; else None
            combat_damage = getattr(resolver, "last_combat_damage", None)
            self.draw(world, combat_damage=combat_damage)

    
            