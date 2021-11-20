from engines.BaseEngine import BaseEngine

class CatEngine(BaseEngine):

    def run_cat(self, options):
        self.machine.to_hq()
        self.machine.to_cattery()
        if options.forts:
            self.machine.to_forts()
            self.machine.level_forts()
        if options.buy_box:
            self.machine.buy_cat()
        if options.queue:
            pass
        self.machine.to_main_menu()