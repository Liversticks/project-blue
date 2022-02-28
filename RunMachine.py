from engines.BattleEngine import BattleEngine
from engines.CatEngine import CatEngine
from engines.RaidEngine import RaidEngine
from mss import mss
from infra.windowManager import WindowMgr
import sqlite3 as sql

db_filename = 'test.db'
seed_script_filename = 'db.sql'

def run_battle(options):
    wm = WindowMgr()
    connection = sql.connect(db_filename)
    connection.isolation_level = None
    connection.row_factory = sql.Row
    with open(seed_script_filename) as seed:
            connection.cursor().executescript(seed.read())
    with mss() as sct:
        be = BattleEngine(options.debug, wm, sct, connection)
        be.clear_stage(options)
        be.cleanup()

def run_cat(options):
    ce = CatEngine(options.debug, None, None)
    ce.run_cat(options)
    print(options)

def run_raid(options):
    re = RaidEngine(options.debug, None, None)
    re.run_raid(options)
