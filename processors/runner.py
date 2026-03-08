import pygame
import sys
from ..graphics.vizconfig import VizConfig, clamp01, lerp, rgb
from ..Entities.world import World
from ..Entities.food import Food
from ..Entities.animal import Animal
from ..data_processors.data_handler import DataHandler
class Runner:
    data_handler: DataHandler
    def __init__(self, W: int, H: int, cfg: VizConfig):
        pygame.init()
        self.W, self.H = W, H
        self.cfg = cfg
        
        self.data_handler = DataHandler()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width, self.screen_height = self.screen.get_size()

        # size of one grid box
        self.cell_w = self.screen_width / self.W
        self.cell_h = self.screen_height / self.H
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
                    restart = True

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
        cw = self.cell_w
        ch = self.cell_h
        self.screen.fill((0, 0, 0))

        # --- Draw food first (so animals draw on top) ---
        for key in list(world.get_food_list().keys()):
            food: Food = world.get_food(key)
            e = food.get_energy()
            # map food energy -> green brightness
            g = clamp01(0.2 + 0.03 * e)
            color = rgb(0, 255 * g, 0)
            rect = pygame.Rect(
                    int(food.get_pos().x * cw),
                    int(food.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
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
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

        # --- Optional grid lines ---
        if self.cfg.grid_lines and self.cell_w >= 6 and self.cell_h >= 6:
            line_color = (25, 25, 25)
            for x in range(self.W + 1):
                px = int(x * cw)
                pygame.draw.line(self.screen, line_color, (px, 0), (px, self.screen_height))

            for y in range(self.H + 1):
                py = int(y * ch)
                pygame.draw.line(self.screen, line_color, (0, py), (self.screen_width, py))

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

    def run(self, world: World, resolver, max_turns=1000, ):
        dt = 0.0
        self.turn = 0
        self.autoplay = False
        self._accum = 0.0
        self.data_handler.save_state(world.get_state())

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
                break

            # Autoplay stepping (fixed turns/sec)
            if self.autoplay:
                self._accum += dt
                step_interval = 1.0 / max(1, self.steps_per_sec)
                while self._accum >= step_interval:
                    self._accum -= step_interval
                    resolver.step(world)  # <- your turn advancement
                    self.turn += 1
                    self.data_handler.save_state(world.get_state())
                    

            # Manual single-step
            if step_once:
                resolver.step(world)
                self.turn += 1
                self.data_handler.save_state(world.get_state())

            # If you have combat damage stored, pass it; else None
            combat_damage = world.get_state().totalCombat
            self.draw(world, combat_damage=combat_damage)
        return self.data_handler

    
            