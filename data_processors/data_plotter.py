from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from ..config import PLOT_DATA
class DataPlotter: 
    path: Path

    def __init__(self, path: Path):
        self.path = path

    def plot(self):
        pass
        
