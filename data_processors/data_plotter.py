from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from .config import DATA, PLOTS
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
class DataPlotter: 
     data_path: Path
     result_path: Path
     def __init__(self, name: str, tau: int):
        self.data_path = DATA / name
        name = name
        self.result_path = DATA / name
        self.tau = tau

     def plot(self):
        turn_data = pd.read_csv(self.data_path / "turn_data.csv")
        spawn_data = pd.read_csv(self.data_path / "spawn_data.csv")
        fig = make_subplots(rows=4,cols=4, shared_xaxes=False, 
                            subplot_titles=PLOTS)
        self.t_plot_afc(fig, turn_data, spawn_data)
        self.t_plot_AE_ET(fig, turn_data, spawn_data)
        self.t_plot_H(fig, turn_data, spawn_data)
        self.t_plot_L(fig, turn_data, spawn_data)
        self.t_plot_V(fig, turn_data, spawn_data)
        self.t_plot_gen(fig, turn_data, spawn_data)
        self.t_plot_FE(fig, turn_data, spawn_data)
        self.t_plot_TAE_TFE_TE(fig, turn_data, spawn_data)
        self.t_food_regen_plot(fig, turn_data, spawn_data)
        self.e_ind_plot(fig, turn_data, spawn_data)
        self.edm_plot(fig, turn_data, spawn_data)
        self.rdm_plot(fig, turn_data, spawn_data)
        self.mode_plot(fig, turn_data, spawn_data)
        self.cooldown_plot(fig, turn_data, spawn_data)
        self.food_add_plot(fig, turn_data, spawn_data)
        self.plot_ET(fig,turn_data, spawn_data)
        self.t_format_and_save(fig)

     def e_ind_plot(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         e_estimator = turn_data["E-indicator"]
         fig.add_trace(go.Scatter(x = turn, y = e_estimator, mode = "lines", name = f"E-indicator"), row = 1, col = 3)

     def rdm_plot(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         RDM = turn_data["RDM"]
         fig.add_trace(go.Scatter(x = turn, y = RDM, mode = "lines", name = f"RDM"), row = 1, col =4)

     def edm_plot(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         EDM = turn_data["EDM"]
         fig.add_trace(go.Scatter(x = turn, y = EDM, mode = "lines", name = f"EDM"), row = 3, col = 4)


     def mode_plot(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         mode = turn_data["mode"]
         fig.add_trace(go.Scatter(x = turn, y = mode, mode = "lines", name = f"Mode"), row = 4, col = 3)

     def cooldown_plot(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         e_estimator = turn_data["cooldown"]
         limit = turn_data["limit"]
         fig.add_trace(go.Scatter(x = turn, y = e_estimator, mode = "lines", name = f"cooldown"), row = 4, col = 2)
         fig.add_trace(go.Scatter(x = turn, y = limit, mode = "lines", name = f"limit"), row = 4, col = 2)
         fig.add_trace(go.Scatter(x = [turn.iloc[0], turn.iloc[-1]], y = [2*self.tau, 2*self.tau], mode = "lines", name = f"full cycle"), row = 4, col = 2)
     
     def food_add_plot(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         e_estimator = turn_data["food added"]
         fig.add_trace(go.Scatter(x = turn, y = e_estimator, 
                                  mode = "lines", name = f"food added", 
                                  line=dict(color = "pink")), row = 1, col = 2)
         
          
     def plot_ET(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
        turn = turn_data["Turn"]
        avgET = turn_data["avgET"]
        maxET = turn_data["maxET"]
        minET = turn_data["minET"]
        fig.add_trace(go.Scatter(x = turn, y = minET, mode = "lines", name = "minET"), row = 4, col = 4)
        fig.add_trace(go.Scatter(x = turn, y = avgET, mode = "lines", name = "avgET"), row = 4, col =4)
        fig.add_trace(go.Scatter(x = turn, y = maxET, mode = "lines", name = "maxET"), row = 4, col = 4)


     def t_plot_afc(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
          turn = turn_data["Turn"]
          animal = turn_data["#animals"]
          food = turn_data["#food"]
          fig.add_trace(go.Scatter(x = turn, y = animal, mode = "lines", name = f"#animals: {spawn_data['Min Val'][0]}"), row = 1, col = 1)
          fig.add_trace(go.Scatter(x = turn, y = food, mode = "lines", name = f"#food: {spawn_data['Min Val'][1]}"), row = 1, col =1)
          

     def t_plot_AE_ET(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
        turn = turn_data["Turn"]
        avgAE = turn_data["avgAE"]
        maxAE = turn_data["maxAE"]
        minAE = turn_data["minAE"]
        fig.add_trace(go.Scatter(x = turn, y = minAE, mode = "lines", name = f"minAE: [{spawn_data['Min Val'][5]},{spawn_data['Max Val'][5]}]"), row = 3, col = 1)
        fig.add_trace(go.Scatter(x = turn, y = avgAE, mode = "lines", name = "avgAE"), row = 3, col =1)
        fig.add_trace(go.Scatter(x = turn, y = maxAE, mode = "lines", name = "maxAE"), row = 3, col = 1)
        

     def t_plot_H(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgH = turn_data["avgH"]
         minH = turn_data["minH"]
         maxH = turn_data["maxH"]
         fig.add_trace(go.Scatter(x = turn, y = minH, mode = "lines", name = f"minH: [{spawn_data['Min Val'][2]},{spawn_data['Max Val'][2]}]"), row = 2, col = 1)
         fig.add_trace(go.Scatter(x = turn, y = avgH, mode = "lines", name = "avgH"), row = 2, col =1)
         fig.add_trace(go.Scatter(x = turn, y = maxH, mode = "lines", name = "maxH"), row = 2, col = 1)
         

     def t_plot_L(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgML = turn_data["avgML"]
         minML = turn_data["minML"]
         maxML = turn_data["maxML"]
         avgL = turn_data["avgL"]
         fig.add_trace(go.Scatter(x = turn, y = minML, mode = "lines", name = f"minML: [{spawn_data['Min Val'][3]},{spawn_data['Max Val'][3]}]"), row = 2, col = 2)
         fig.add_trace(go.Scatter(x = turn, y = avgML, mode = "lines", name = "avgML"), row = 2, col =2)
         fig.add_trace(go.Scatter(x = turn, y = maxML, mode = "lines", name = "maxML"), row = 2, col = 2)
         fig.add_trace(go.Scatter(x = turn, y = avgL, mode = "lines", name = "avgL"), row = 2, col = 2)

     def t_plot_V(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgV = turn_data["avgV"]
         minV = turn_data["minV"]
         maxV = turn_data["maxV"]
         fig.add_trace(go.Scatter(x = turn, y = minV, mode = "lines", name = f"minV: [{spawn_data['Min Val'][4]},{spawn_data['Max Val'][4]}]"), row = 2, col = 3)
         fig.add_trace(go.Scatter(x = turn, y = avgV, mode = "lines", name = "avgV"), row = 2, col =3)
         fig.add_trace(go.Scatter(x = turn, y = maxV, mode = "lines", name = "maxV"), row = 2, col = 3)

     def t_plot_gen(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgGen = turn_data["avgGen"]
         minGen = turn_data["minGen"]
         maxGen = turn_data["maxGen"]
         fig.add_trace(go.Scatter(x = turn, y = minGen, mode = "lines", name = f"minGen"), row = 2, col = 4)
         fig.add_trace(go.Scatter(x = turn, y = avgGen, mode = "lines", name = "avgGen"), row = 2, col =4)
         fig.add_trace(go.Scatter(x = turn, y = maxGen, mode = "lines", name = "maxGen"), row = 2, col = 4)

     def t_plot_FE(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         avgFE = turn_data["avgFE"]
         minFE = turn_data["minFE"]
         maxFE = turn_data["maxFE"]
         fig.add_trace(go.Scatter(x = turn, y = minFE, mode = "lines", name = f"minFE: [{spawn_data['Min Val'][5]},{spawn_data['Max Val'][5]}]"), row = 3, col = 2)
         fig.add_trace(go.Scatter(x = turn, y = avgFE, mode = "lines", name = "average food energy"), row = 3, col = 2)
         fig.add_trace(go.Scatter(x = turn, y = maxFE, mode = "lines", name = "maximum food energy"), row = 3, col = 2)
         

     def t_plot_TAE_TFE_TE(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         totalAE = turn_data["totalAE"]
         totalFE = turn_data["totalFE"]
         totalE = turn_data["totalE"]
         fig.add_trace(go.Scatter(x = turn, y = totalAE, mode = "lines", name = "total animal energy"), row = 3, col = 3)
         fig.add_trace(go.Scatter(x = turn, y = totalFE, mode = "lines", name = "total food energy"), row = 3, col = 3)
         fig.add_trace(go.Scatter(x = turn, y = totalE, mode = "lines", name = "total energy"), row = 3, col = 3)

     def t_food_regen_plot(self,fig, turn_data: pd.DataFrame, spawn_data: pd.DataFrame):
         turn = turn_data["Turn"]
         totalcombat = turn_data["totalCombat"] 
         min_bound = turn_data["min_bound"].shift(1)
         avg_bound = turn_data["avg_bound"].shift(1)
         max_bound = turn_data["max_bound"].shift(1)
         fig.add_trace(go.Scatter(x = turn, y = min_bound, mode = "lines", name = "min_bound"), row = 4, col = 1)
         fig.add_trace(go.Scatter(x = turn, y = avg_bound, mode = "lines", name = "avg_bound"), row = 4, col = 1)
         fig.add_trace(go.Scatter(x = turn, y = max_bound, mode = "lines", name = "max_bound"), row = 4, col = 1)
         fig.add_trace(go.Scatter(x = turn, y = totalcombat, mode = "lines", name = "total Combat"), row = 4, col =1)
         

     def t_format_and_save(self, fig):
        fig.update_layout(
                         legend=dict(
                              orientation="h",
                              yanchor="top",
                              y=-0.15,
                              xanchor="center",
                              x=0.5,
                              font=dict(size=9)
                                   )
                         )
        for i in range (1,4):
             for j in range(1,4):
                  fig.update_xaxes(title = "Turn", row = i, col = j)

        fig.write_html(str(self.result_path / "summary.html"), auto_open = True)







        
