from BattleEngine import BattleEngine
from CatEngine import CatEngine
from RaidEngine import RaidEngine
from mss import mss

def run_battle(options):
    with mss() as sct:
        be = BattleEngine(sct)
        be.clear_stage(options)
        be.cleanup()

def run_cat(options):
    print()

def run_raid(options):
    re = RaidEngine(None)
    re.run_raid(options)
