from BattleEngine import BattleEngine
from CatEngine import CatEngine
from mss import mss

def run_battle(options):
    with mss() as sct:
        be = BattleEngine(sct)
        be.clear_stage(options)

def run_cat(options):
    print()