from engines.BattleEngine import BattleEngine
from engines.CatEngine import CatEngine
from engines.RaidEngine import RaidEngine
from mss import mss

def run_battle(options):
    with mss() as sct:
        be = BattleEngine(sct)
        be.clear_stage(options)
        be.cleanup()

def run_cat(options):
    ce = CatEngine(None)
    ce.run_cat(options)
    print(options)

def run_raid(options):
    re = RaidEngine(None)
    re.run_raid(options)
