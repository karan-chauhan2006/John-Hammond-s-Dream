from dataclasses import dataclass

@dataclass
class State:
    turn: int = -1
    animals: int = 0
    food: int = 0
    avgAE: float = None
    avgET: float = None
    avgH: float = None
    avgV: float = None
    avgL: float = None
    avgFE: float = None
    avgGen: float = None
    maxAE: float = 0.0
    maxET: float = 0.0
    maxH: int = 0
    maxV: int = 0
    maxL: int = 0
    maxFE: float = 0.0
    maxGen: int = 0
    minAE: float = 10e10
    minET: float = 10e10
    minH: int = 10e10
    minV: int = 10e10
    minL: int = 10e10
    minFE: float = 10e10
    minGen: int = 10e10
    totalAE: float = None
    totalFE: float = None
    totalCombat: float = 0.0
    totalE: float = None

    def get_arr(self) -> list:
        return [self.turn, self.animals, self.food, self.avgAE, self.avgET,
                self.avgH, self.avgV, self.avgL, self.avgFE, self.avgGen,
                self.maxAE, self.maxET, self.maxH, self.maxV, self.maxL,
                self.maxFE, self.maxGen, self.minAE, self.minET, self.minH,
                self.minV, self.minL, self.minFE, self.minGen, self.totalAE,
                self.totalFE, self.totalE, self.totalCombat]

    def set_total_combat(self, combat: int):
        self.totalCombat = combat

    def print(self):
         print(
        f"Turn {self.turn:03d} | "
        f"Animals: {self.animals:4d} | "
        f"Food: {self.food:4d} | "
        f"Avg animal energy: {self.avgAE:7.2f} | "
        f"Avg energy threshold: {self.avgET:7.2f} | "
        f"Avg hit: {self.avgH:7.2f} | "
        f"Avg vision: {self.avgV:7.2f} | "
        f"Avg life: {self.avgL:7.2f} | "
        f"Avg food energy: {self.avgFE:7.2f} | "
        f"Avg Gen: {self.avgGen:7.2f} | "
        f"Max animal energy: {self.maxAE:7.2f} | "
        f"Max energy threshold: {self.maxET:7.2f} | "
        f"Max hit: {self.maxH:4d} | "
        f"Max vision: {self.maxV:4d} | "
        f"Max life: {self.maxL:4d} | "
        f"Max food energy: {self.maxFE:7.2f} | "
        f"Max gen on map: {self.maxGen:4d} | "
        f"Min animal energy: {self.minAE:7.2f} | "
        f"Min energy threshold: {self.minET:7.2f} | "
        f"Min hit: {self.minH:4d} | "
        f"Min vision: {self.minV:4d} | "
        f"Min life: {self.minL:4d} | "
        f"Min food energy: {self.minFE:7.2f} | "
        f"Min gen on map: {self.minGen:4d} | "
        f"total animal energy: {self.totalAE:7.2f} | "
        f"toal food energy: {self.totalFE:7.2f} | "
        f"total energy: {self.totalE:7.2f} | "
        f"total combat: {self.totalCombat:7.2f} | "
    )
    

