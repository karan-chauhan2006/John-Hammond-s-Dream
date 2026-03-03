from pathlib import Path

ROOT = Path(__file__).resolve().parents[0]

DATA = ROOT / "data"
RAW_DATA = DATA / "raw"
PLOT_DATA = DATA / "plot"

CLOUMNS = ["Turn", "#animals", "#food", "avgAE", "avgET", "avgH",
               "avgV", "avgML", "avgL", "avgFE", "avgGen", "maxAE", "maxET", "maxH",
               "maxV", "maxML", "maxFE", "maxGen", "minAE", "minET", "minH",
               "minV", "minML", "minFE", "minGen", "totalAE", "totalFE", 
               "totalE", "totalCombat"]

STABILITY_FACTOR = 0.25
MAXPRL = 0.4
MINPRL = 0.01
TAU = 25
#advised to always keep the list in increasing order, (and use all integers between max and min)
REPRODUCTION_CONSTANT = 4
MUTATION_CONSTANT = 0.01
MUTATION_CHOICE = [-1,0,1] 