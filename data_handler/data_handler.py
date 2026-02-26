import pandas as pd
from ..Entities.state import State
class DataHandler: 
    data = list[list]
    columns = ["Turn", "#animals", "#food", "avgAE", "avgET", "avgH",
               "avgV", "avgL", "avgFE", "avgGen", "maxAE", "maxET", "maxH",
               "maxV", "maxL", "maxFE", "maxGen", "minAE", "minET", "minH",
               "minV", "minL", "minFE", "minGen", "totalAE", "totalFE", 
               "totalE", "totalCombat"]
    
    def __init__(self):
        self.data = []

    def save_state(self, state: State):
        self.data.append(state.get_arr())
        
    def save_data(self): 
        print(pd.DataFrame(self.data, columns= self.columns))