from dataclasses import dataclass

@dataclass
class VizConfig:
    cell_size: int = 20
    grid_lines: bool = True
    fps: int = 5
    autoplay_steps_per_sec: int = 1  # how many turns/sec when autoplay is on
    show_grid_every_n: int = 1        # draw every Nth turn if sim is heavy

def clamp01(x: float) -> float:
    return 0.0 if x < 0 else 1.0 if x > 1 else x

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

def rgb(r, g, b):
    return (int(r), int(g), int(b))
