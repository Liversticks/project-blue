from BaseEngine import BaseEngine

class BattleEngine(BaseEngine):

    eventPrefixes = ['A', 'B', 'C', 'D', 'SP']
    
    def enter_normal_stage(self, fleet1, fleet2=None):
        self.machine.to_select_fleet()
        self.machine.clear_2()
        self.machine.set_surface_1(fleet=fleet1)
        if fleet2 is not None:
            self.machine.set_surface_2(fleet=str(fleet2[0]))
        self.machine.set_roles()
    
    def clear_normal_stage(self, iterations, heclp=False):
        self.machine.enter_combat()
        self.machine.finish_combat()
        for _ in range(iterations - 1):
            if heclp:
                self.machine.set_heclp()
            self.machine.continue_stage()
        self.machine.finish_combat()

    def clear_stage(self, options):
        for stage in options.split:
            components = stage.split('-')
            prefix = components[0]
            stage_number = components[1]
            if prefix in self.eventPrefixes:
                self.machine.to_event()
                if prefix != 'SP':
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
                if prefix in ['A', 'B', 'SP']:
                    self.enter_normal_stage(str(options.fleet1[0]), options.fleet2)
                else:
                    self.machine.to_select_fleet()
                self.clear_normal_stage(options.iterations, options.heclp)
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
                self.clear_normal_stage(options.iterations, options.heclp)
                self.machine.exit_stage()
                self.machine.to_main_menu()