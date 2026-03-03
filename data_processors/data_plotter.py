from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from ..config import PLOT_DATA, STABILITY_FACTOR
import numpy as np
class DataPlotter: 
    data_path: Path
    result_path: Path
    def __init__(self, path: Path):
        self.data_path = path
        name = path.name
        self.result_path = PLOT_DATA / name
        self.result_path.mkdir(parents= True, exist_ok= True)

    def plot(self):
        fig, axs = plt.subplots(3,3, figsize=(18, 8))
        turn_data = pd.read_csv(self.data_path / "turn_data.csv")
        spawn_data = pd.read_csv(self.data_path / "spawn_data.csv")
        self.plot_afc(axs[0,0], turn_data, spawn_data)
        self.plot_AE_ET(axs[0,1], turn_data, spawn_data)
        self.plot_H(axs[0,2], turn_data, spawn_data)
        self.plot_L(axs[1,0], turn_data, spawn_data)
        self.plot_V(axs[1,1], turn_data, spawn_data)
        self.plot_gen(axs[1,2], turn_data, spawn_data)
        self.plot_FE(axs[2,0], turn_data, spawn_data)
        self.plot_TAE_TFE_TE(axs[2,1], turn_data, spawn_data)
        self.test_plot(axs[2,2], turn_data, spawn_data)
        self.format_and_save(fig, axs)

    def plot_afc(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
        turn = turn_data["Turn"]
        animal = turn_data["#animals"]
        food = turn_data["#food"]
        combat = turn_data["totalCombat"]
        axs.plot(turn, animal, label = f"#animals: {spawn_data['Min Val'][0]}")
        axs.plot(turn, food, label = f"#food: {spawn_data['Min Val'][1]}")
        axs.plot(turn, combat, label = f"total combat")
        axs.legend(loc = "upper right", fontsize=5)
        axs.set_title("turn V/S #animals, #food & total Combat")
        axs.set_xlabel("Turns")
        axs.grid(alpha=0.3)

    def plot_AE_ET(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
        turn = turn_data["Turn"]
        avgAE = turn_data["avgAE"]
        avgET = turn_data["avgET"]
        maxAE = turn_data["maxAE"]
        maxET = turn_data["maxET"]
        minAE = turn_data["minAE"]
        minET = turn_data["minET"]
        axs.plot(turn, minAE, 
                 label = f"minAE: [{spawn_data['Min Val'][5]},{spawn_data['Max Val'][5]}]")
        axs.plot(turn, avgAE, label = "avgAE")
        axs.plot(turn, maxAE, label = "maxAE")
        axs.plot(turn, minET, label = f"minET")
        axs.plot(turn, avgET, label = f"avgET")
        axs.plot(turn, maxET, label = f"maxET")
        axs.legend(loc = "upper right", fontsize=5)
        axs.set_title("turn V/S animal energy data & energy threshold data")
        axs.set_xlabel("Turns")
        axs.grid(alpha=0.3)

    def plot_H(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgH = turn_data["avgH"]
         minH = turn_data["minH"]
         maxH = turn_data["maxH"]
         axs.plot(turn, minH, 
                    label = f"minH: [{spawn_data['Min Val'][2]},{spawn_data['Max Val'][2]}]")
         axs.plot(turn, avgH, label = "avgH")
         axs.plot(turn, maxH, label = "maxH")
         axs.legend(loc = "lower right", fontsize=5)
         axs.set_title("turn V/S Hit data")
         axs.set_xlabel("Turns")
         axs.grid(alpha=0.3)

    def plot_L(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgML = turn_data["avgML"]
         minML = turn_data["minML"]
         maxML = turn_data["maxML"]
         avgL = turn_data["avgL"]
         axs.plot(turn, minML, 
                    label = f"minML: [{spawn_data['Min Val'][3]},{spawn_data['Max Val'][3]}]")
         axs.plot(turn, avgML, label = "avgML")
         axs.plot(turn, maxML, label = "maxML")
         axs.plot(turn, avgL, label = "avgL")
         axs.legend(loc = "lower center", fontsize=5)
         axs.set_title("turn V/S max Life data")
         axs.set_xlabel("Turns")
         axs.grid(alpha=0.3)

    def plot_V(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgV = turn_data["avgV"]
         minV = turn_data["minV"]
         maxV = turn_data["maxV"]
         axs.plot(turn, minV, 
                    label = f"minV: [{spawn_data['Min Val'][4]},{spawn_data['Max Val'][4]}]")
         axs.plot(turn, avgV, label = "avgV")
         axs.plot(turn, maxV, label = "maxV")
         axs.legend(loc = "lower left", fontsize=5)
         axs.set_title("turn V/S vision data")
         axs.set_xlabel("Turns")
         axs.grid(alpha=0.3)

    def plot_gen(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgGen = turn_data["avgGen"]
         minGen = turn_data["minGen"]
         maxGen = turn_data["maxGen"]
         axs.plot(turn, minGen, 
                    label = f"minGen")
         axs.plot(turn, avgGen, label = "avgGen")
         axs.plot(turn, maxGen, label = "maxGen")
         axs.legend(loc = "upper left", fontsize=5)
         axs.set_title("turn V/S Generation data")
         axs.set_xlabel("Turns")
         axs.grid(alpha=0.3)

    def plot_FE(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgFE = turn_data["avgFE"]
         minFE = turn_data["minFE"]
         maxFE = turn_data["maxFE"]
         axs.plot(turn, minFE, 
                    label = f"minFE: [{spawn_data['Min Val'][5]},{spawn_data['Max Val'][5]}]")
         axs.plot(turn, avgFE, label = "avgFE")
         axs.plot(turn, maxFE, label = "maxFE")
         axs.legend(loc = "upper right", fontsize=5)
         axs.set_title("turn V/S food energy data")
         axs.set_xlabel("Turns")
         axs.grid(alpha=0.3)

    def plot_TAE_TFE_TE(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         totalAE = turn_data["totalAE"]
         totalFE = turn_data["totalFE"]
         totalE = turn_data["totalE"]
         axs.plot(turn, totalFE, 
                    label = f"total food energy")
         axs.plot(turn, totalAE, label = "total animal energy")
         axs.plot(turn, totalE, label = "total energy")
         axs.legend(loc = "upper right", fontsize=5)
         axs.set_title("turn V/S energy data")
         axs.set_xlabel("Turns")
         axs.grid(alpha=0.3)

    def test_plot(self,axs, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         totalcombat = turn_data["totalCombat"]
         animal = turn_data["#animals"]
         minH = turn_data["minH"]
         avgH = turn_data["avgH"]
         maxH = turn_data["maxH"]
         neighbour_factor = totalcombat / animal
         base = neighbour_factor-1
         base = base.clip(upper = 4, lower = 1) 
         min_bound = base*minH*animal*STABILITY_FACTOR
         avg_bound = base*avgH*animal*STABILITY_FACTOR
         max_bound = base*maxH*animal*STABILITY_FACTOR

         axs.plot(turn, min_bound, 
                    label = f"min_bound")
         axs.plot(turn, avg_bound, label = "avg_bound")
         axs.plot(turn, max_bound, label = "max_bound")
         axs.plot(turn, totalcombat, label = "total Combat")
         axs.legend(loc = "upper right", fontsize=5)
         axs.set_title("turn V/S food regen")
         axs.set_xlabel("Turns")
         axs.grid(alpha=0.3)

    def format_and_save(self, fig, axs):
        fig.suptitle("Ecosystem Simulation Summary", fontsize=16)
        fig.tight_layout(rect=[0, 0, 1, 0.96])
        fig.savefig(self.result_path / "summary.png", dpi = 300, bbox_inches="tight")






        
