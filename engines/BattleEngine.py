from engines.BaseEngine import BaseEngine
import sqlite3 as sql

class UnexpectedStateError(Exception):
    pass

class BattleEngine(BaseEngine):

    db_filename = 'test.db'
    seed_script_filename = 'db.sql'
    eventPrefixes = ['A', 'B', 'C', 'D', 'SP', 'T']
    selectStage = 'SELECT is_hard, clear_time FROM stage WHERE stage = ?'

    def enter_normal_stage(self, fleet1, fleet2=None):
        self.machine.to_select_fleet()
        self.machine.clear_2()
        self.machine.set_surface_1(fleet=fleet1)
        if fleet2 is not None:
            self.machine.set_surface_2(fleet=str(fleet2[0]))
        self.machine.set_roles()
    
    def enter_first_stage(self, min_clear_time):
        self.machine.enter_combat(min_clear_time=min_clear_time)
    
    def finish_stage(self):
        while self.machine.state == 'combat':
            self.machine.finish_combat()
        
        if self.machine.state == 'stage-defeat':
            self.machine.cleanup_defeat()
        elif self.machine.state == 'stage-clear':
            self.logger.info("Stage cleared.")
        else:
            raise UnexpectedStateError

    def clear_subsequent_stage(self, heclp=False):
        if heclp:
            self.machine.set_heclp()
        self.machine.continue_stage()
        self.finish_stage()

    def clear_normal_stage(self, min_clear_time, iterations, heclp=False):
        self.enter_first_stage(min_clear_time)
        self.finish_stage()

        for _ in range(iterations - 1):
            self.clear_subsequent_stage(heclp=heclp)

    def clear_stage(self, options):
        for stage in options.split:
            self.logger.debug(f'Attempting to clear stage {stage}')
            
            self.cursor.execute(self.selectStage, (stage,))
            row = self.cursor.fetchone()
            self.logger.debug(f'Column names returned: {row.keys()}')
            components = stage.split('-')
            prefix = components[0]
            stage_number = components[1]
            
            if prefix in self.eventPrefixes:
                self.machine.to_event()
                if prefix == 'T':
                    self.machine.to_T()
                elif prefix != 'SP':
                    # WARNING: not yet implemented
                    self.machine.to_SP()
                    if prefix == 'D':
                        self.machine.to_D()
                    elif prefix == 'C':
                        self.machine.to_D()
                        self.machine.to_C()
                    elif prefix == 'B':
                        self.machine.to_B()
                    elif prefix == 'A':
                        self.machine.to_B()
                        self.machine.to_A()
                getattr(self.machine, f'enter_{stage_number}')()
                if row['is_hard']:
                    self.machine.to_select_fleet()
                else:
                    self.enter_normal_stage(str(options.fleet1[0]), options.fleet2)
                self.clear_normal_stage(row['clear_time'], options.iterations, options.heclp)
                self.machine.exit_stage()
                self.machine.to_main_menu()
            else:
                self.machine.to_battle()
                self.machine.to_campaign()
                self.machine.to_chapter_1()
                for _ in range(int(prefix) - 1):
                    self.machine.next_chapter()
                getattr(self.machine, f'enter_{stage_number}')()
                # TODO: make passing in fleet2 less painful
                self.enter_normal_stage(str(options.fleet1[0]), options.fleet2)
                self.clear_normal_stage(row['clear_time'], options.iterations, options.heclp)
                self.machine.exit_stage()
                self.machine.to_main_menu()

    def cleanup(self):
        self.connection.close()

    def __init__(self, sct):
        super().__init__(sct)
        self.connection = sql.connect(self.db_filename)
        self.connection.isolation_level = None
        self.connection.row_factory = sql.Row
        self.cursor = self.connection.cursor()
        with open(self.seed_script_filename) as seed:
            self.cursor.executescript(seed.read())