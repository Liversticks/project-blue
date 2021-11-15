from engines.BaseEngine import BaseEngine
import datetime as dt

class RaidEngine(BaseEngine):
    
    def to_target_raid(self, target):
        while (self.machine.state != target):
            self.machine.raids_right()
    
    def run_raid(self, options):
        # Convert to server time (Lexington - Mountain Time)
        server_time = dt.timezone(dt.timedelta(hours=-7))
        now = dt.datetime.now(tz=server_time)
        
        self.machine.to_battle()
        self.machine.to_daily_raids()
        
        # Run tactical training (all day)
        self.machine.to_levels()
        self.machine.quick_attack(option='3')
        self.machine.to_daily_raids()

        # If day == [Sunday, Monday, Thursday], run Escort Mission
        if now.weekday() in [0, 3, 6]:
            self.to_target_raid('daily-raids-e')
            self.machine.to_levels()
            self.machine.quick_attack(option='1')
            self.machine.to_daily_raids()

        # If day == [Sunday, Tuesday, Friday], run Advance Mission
        if now.weekday() in [1, 4, 6]:
            self.to_target_raid('daily-raids-a')
            self.machine.to_levels()
            self.machine.quick_attack(option='1')
            self.machine.to_daily_raids()

        # If day == [Sunday, Wednesday, Saturday], run Fierce Assault
        if now.weekday() in [2, 5, 6]:
            self.to_target_raid('daily-raids-f')
            self.machine.to_levels()
            self.machine.quick_attack(option='1')
            self.machine.to_daily_raids()
        
        # TODO: handle submarine weekly raids

        self.machine.to_main_menu()

        