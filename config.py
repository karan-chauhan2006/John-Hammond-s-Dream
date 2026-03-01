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
MAXPRL = 0.10
MINPRL = 0.01
TAU = 5
