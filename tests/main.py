import unittest
import machine.StateMachine as m
import transitions

class TestStateMachine(unittest.TestCase):

    @classmethod
    def setUp(self):
        # Do not call any stage clear transition or one that relies on time_and_screenshot!
        self.machine = m.StateMachine(None, None)

    def test_start(self):
        self.assertEqual(self.machine.state, 'main-menu')

    def test_main_menu_fail(self):
        with self.assertRaises(transitions.core.MachineError):
            self.machine.to_exercises()
        
        with self.assertRaises(transitions.core.MachineError):
            self.machine.to_cattery()

        with self.assertRaises(transitions.core.MachineError):
            self.machine.to_daily_raids()

        with self.assertRaises(transitions.core.MachineError):
            self.machine.to_campaign()

    def test_main_menu_hq(self):
        self.machine.to_hq()
        self.assertEqual(self.machine.state, 'hq')

    def test_main_menu_battle(self):
        self.machine.to_battle()
        self.assertEqual(self.machine.state, 'battle')

    def test_main_menu_quick_access(self):
        self.machine.to_quick_access()
        self.assertEqual(self.machine.state, 'quick-access')

    def test_main_menu_quick_access(self):
        self.machine.to_event()
        self.assertEqual(self.machine.state, 'current-event-*')

if __name__ == '__main__':
    unittest.main()