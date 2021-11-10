from BaseEngine import BaseEngine

class BattleEngine(BaseEngine):

    eventPrefixes = ['A', 'B', 'C', 'D']
    
    def clear_stage(self, options):
        for stage in options.split:
            components = stage.split('-')
            if components[0] in self.eventPrefixes:
                self.machine.to_event()
                print("hi")
            else:
                self.machine.to_battle()
                self.machine.to_campaign()
                self.machine.to_chapter_1()
                for _ in range(int(components[0]) - 1):
                    self.machine.next_chapter()
                getattr(self.machine, f'enter_{components[1]}')()
                self.machine.to_select_fleet()
                self.machine.clear_2()
                self.machine.set_surface_1(fleet=str(options.fleet1[0]))
                if options.fleet2 is not None:
                    self.machine.set_surface_2(fleet=str(options.fleet2[0]))
                self.machine.set_roles()
                self.machine.enter_combat()
                self.machine.finish_combat()
                for _ in range(options.iterations - 1):
                    if options.heclp:
                        self.machine.set_heclp()
                    self.machine.continue_stage()
                    self.machine.finish_combat()
                self.machine.exit_stage()
                self.machine.to_main_menu()