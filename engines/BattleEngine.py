from engines.BaseEngine import BaseEngine
import time

class UnexpectedStateError(Exception):
    pass

class BattleEngine(BaseEngine):
    eventPrefixes = ['A', 'B', 'C', 'D', 'SP', 'T']
    selectStage = 'SELECT is_hard, default_clear_time FROM stage WHERE stage = ?'
    trackClearTime = 'INSERT INTO attempt_history (stage, end_time, clear_time) VALUES (?, ?, ?)'

    def record_clear_time(self, stage, end_time, clear_time):
        self.cursor.execute(self.trackClearTime, (stage, end_time, clear_time))

    def enter_normal_stage(self, fleet1, fleet2=None):
        self.machine.to_select_fleet()
        self.machine.clear_2()
        self.machine.set_surface_1(fleet=fleet1)
        if fleet2 is not None:
            self.machine.set_surface_2(fleet=str(fleet2[0]))
        self.machine.set_roles_main()
    
    def do_battle(self, default_clear_time, useDefault):
        if useDefault:
            self.machine.default_time_clear(wait=default_clear_time)
        else:
            self.machine.poll_clear()
            while self.machine.state == 'combat-poll':
                self.machine.poll_clear()
            self.machine.finish_combat()
            if self.machine.state == 'stage-defeat':
                self.machine.cleanup_defeat()
            elif self.machine.state == 'stage-clear':
                self.logger.info("Stage cleared.")
            else:
                raise UnexpectedStateError
        assert (self.machine.state == 'stage-clear')

    nanoseconds_per_second = 1000000000

    def clear_subsequent_stage(self, stage, default_clear_time, useDefault, heclp=False, shuffle=False):
        if shuffle:
            print()
            # exit to chapter (from stage)
            # renter stage (from stage)
            # set_roles_alt
        
        if heclp:
            self.machine.set_heclp()
        start_time = time.time_ns()
        self.machine.continue_stage()
        self.do_battle(default_clear_time, useDefault)
        end_time = time.time_ns()
        if not useDefault:
            self.record_clear_time(stage, end_time // self.nanoseconds_per_second, (end_time - start_time) // self.nanoseconds_per_second)

    def clear_normal_stage(self, stage, default_clear_time, iterations, heclp=False, useDefault=False):
        start_time = time.time_ns()
        self.machine.enter_combat()
        self.do_battle(default_clear_time, useDefault)
        end_time = time.time_ns()
        if not useDefault:
            self.record_clear_time(stage, end_time // self.nanoseconds_per_second, (end_time - start_time) // self.nanoseconds_per_second)

        for _ in range(iterations - 1):
            self.clear_subsequent_stage(stage, default_clear_time, useDefault, heclp=heclp)

    def handle_EX_event(self, prefix):
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
                    self.handle_EX_event(prefix)    
                getattr(self.machine, f'enter_{stage_number}')()
                if row['is_hard']:
                    self.machine.to_select_fleet()
                else:
                    self.enter_normal_stage(str(options.fleet1[0]), options.fleet2)
            else:
                self.machine.to_battle()
                self.machine.to_campaign()
                self.machine.to_chapter_1()
                for _ in range(int(prefix) - 1):
                    self.machine.next_chapter()
                getattr(self.machine, f'enter_{stage_number}')()
                self.enter_normal_stage(str(options.fleet1[0]), options.fleet2)
            self.clear_normal_stage(stage, row['default_clear_time'], options.iterations, heclp=options.heclp, useDefault=options.timeout)
            self.machine.exit_stage()
            self.machine.to_main_menu()

    def cleanup(self):
        self.connection.close()

    def __init__(self, debug, wm, sct, connection):
        super().__init__(debug, wm, sct)
        self.connection = connection
        self.cursor = self.connection.cursor()
