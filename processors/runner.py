import pygame
import sys
from ..graphics.vizconfig import VizConfig, clamp01, lerp, rgb
from ..graphics.colours import Colours
from ..Entities.world import World
from ..Entities.food import Food
from ..Entities.animal import Animal
from ..data_processors.data_handler import DataHandler
from ..processors.turn_resolver import TurnResolver
from ..Entities.genealogy import Genealogy
from ..usecase.flush import FlushUseCase
from .config import MODES, P_MODES
class Runner:
    data_handler: DataHandler
    flush: FlushUseCase
    modes: list[str]
    current_mode_num: int
    colours: Colours

    def __init__(self, W: int, H: int, cfg: VizConfig, data_handler: DataHandler, version: str):
        pygame.init()
        self.W, self.H = W, H
        self.cfg = cfg
        
        self.data_handler = data_handler
        self.flush = FlushUseCase()
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

        if version == "V5":
            self.modes = P_MODES
        else:
            self.modes = MODES
        self.current_mode_num = 0
        self.colours = Colours()

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
                
                if event.key == pygame.K_c:
                    self.current_mode_num += 1
                    if self.current_mode_num == len(self.modes):
                        self.current_mode_num = 0

        return step_once, restart

    def draw(self, world: World, combat_damage=None):
        cw = self.cell_w
        ch = self.cell_h
        self.screen.fill((0, 0, 0))
        self.draw_plants(world)

        match(self.modes[self.current_mode_num]):
            case "Energy":
                self.energy_draw(world)
            case "Threshold":
                self.threshold_draw(world)
            case "Hit": 
                self.hit_draw(world)
            case "Life":
                self.life_draw(world)
            case "Max Life":
                self.max_life_draw(world)
            case "Vision":
                self.vision_draw(world)
            case "Gen": 
                self.gen_draw(world)


            

        

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
        hud += f" | Mode = {self.modes[self.current_mode_num]}"
        if combat_damage is not None:
            hud += f" | dmg={combat_damage}"

        # Draw HUD with a slight shadow for readability
        surf1 = self.font.render(hud, True, (0, 0, 0))
        surf2 = self.font.render(hud, True, (220, 220, 220))
        self.screen.blit(surf1, (9, 9))
        self.screen.blit(surf2, (8, 8))

        pygame.display.flip()

    def draw_plants(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
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

    def energy_draw(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
        max_eng = world.get_state().maxAE
        min_eng = world.get_state().minAE
        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)

            color = self.colours.yellow(a.energy, min_eng, max_eng)
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

       
        
    def threshold_draw(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
        max_threshold = world.get_state().maxET
        min_threshold = world.get_state().minET
        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)

            color = self.colours.orange(a.threshold, min_threshold, max_threshold)
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

        
    
    def hit_draw(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
        max_hit = world.get_state().maxH
        min_hit = world.get_state().minH
        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)

            color = self.colours.red(a.hit, min_hit, max_hit)
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

        
        
    def life_draw(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
        max_life = world.get_state().maxL
        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)

            l = a.get_life()
            b = int(l*255/max_life)
            color = rgb(0, 0, b)
        
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

    def max_life_draw(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
        max_life = world.get_state().maxL
        min_life = world.get_state().minL
        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)

            color = self.colours.purple(a.max_life, min_life, max_life)
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

       
    def vision_draw(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
        max_vision = world.get_state().maxV
        min_vision = world.get_state().minV
        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)

            color = self.colours.cyan(a.vision, min_vision, max_vision)
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

        
        

    def gen_draw(self, world: World):
        cw = self.cell_w
        ch = self.cell_h
        max_vision = world.get_state().maxGen
        min_vision = world.get_state().minGen
        # --- Draw animals ---
        for key in list(world.get_animal_list().keys()):
            a: Animal = world.get_animal(key)

            color = self.colours.magenta(a.gen, min_vision, max_vision)
            rect = pygame.Rect(
                    int(a.get_pos().x * cw),
                    int(a.get_pos().y * ch),
                    int(cw) + 1,
                    int(ch) + 1
                    )
            pygame.draw.rect(self.screen, color, rect)

        
        
    

    def run(self, world: World, genealogy: Genealogy, resolver: TurnResolver, max_turns=1000, ):
        dt = 0.0
        self.turn = 0
        self.autoplay = True
        self._accum = 0.0
        self.data_handler.record_turn_data(world.get_state())

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
                    resolver.step(world, genealogy)
                    self.turn += 1
                    self.data_handler.record_turn_data(world.get_state())
                    self.data_handler.record_gen_data(genealogy.empty_genes())
                    

            # Manual single-step
            if step_once:
                resolver.step(world, genealogy)
                self.turn += 1
                self.data_handler.record_turn_data(world.get_state())
                self.data_handler.record_gen_data(genealogy.empty_genes())

            # If you have combat damage stored, pass it; else None
            combat_damage = world.get_state().totalCombat
            self.draw(world, combat_damage=combat_damage)
        
        self.flush.execute(world,genealogy)
        self.data_handler.record_gen_data(genealogy.empty_genes())

    
            