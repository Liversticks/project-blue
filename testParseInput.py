import unittest as u
import parseInput

class TestParseInput(u.TestCase):

    def test_no_submodule(self):
        a = parseInput.parse_arguments([])
        self.assertIsNone(a.subparser)
        self.assertFalse(a.debug)
    
    @u.expectedFailure
    def test_invalid_submodule(self):
        parseInput.parse_arguments(['bruh'])

    def test_debug_on(self):
        a = parseInput.parse_arguments(['-d'])
        self.assertTrue(a.debug)

    @u.expectedFailure
    def test_cat_invalid_flag(self):
        parseInput.parse_arguments(['cat', '-asd'])

    @u.expectedFailure
    def test_raid_invalid_flag(self):
        parseInput.parse_arguments(['raid', '-abc'])

    @u.expectedFailure
    def test_battle_invalid_iterations(self):
        a = parseInput.parse_arguments(['battle', '1-1', '-5', 'f1', '1'])
        parseInput.validate_campaign_or_event(a)

    @u.expectedFailure
    def test_battle_no_iterations(self):
        parseInput.parse_arguments(['battle', '1-1', '-f1', '6'])

    @u.expectedFailure
    def test_battle_invalid_stage(self):
        a = parseInput.parse_arguments(['battle', '1-5', '3', '-f1', '3'])
        parseInput.validate_campaign_or_event(a)

    @u.expectedFailure
    def test_battle_no_f1(self):
        parseInput.parse_arguments(['battle', '1-2', '6'])

    def test_battle_f1_f2_distinct(self):
        a = parseInput.parse_arguments(['battle', '13-3', '4', '-f1', '3', '-f2', '4'])
        parseInput.validate_campaign_or_event(a)
        self.assertEqual(a.fleet1, [3])
        self.assertEqual(a.fleet2, [4])

    @u.expectedFailure
    def test_battle_f1_f2_same(self):
        a = parseInput.parse_arguments(['battle', '13-3', '4', '-f1', '3', '-f2', '3'])
        parseInput.validate_campaign_or_event(a)
        
    @u.expectedFailure
    def test_battle_f1_out_of_range(self):
        a = parseInput.parse_arguments(['battle', '13-3', '4', '-f1', '7', '-f2', '4'])
        parseInput.validate_campaign_or_event(a)
    
    @u.expectedFailure
    def test_battle_f2_out_of_range(self):
        a = parseInput.parse_arguments(['battle', '13-3', '4', '-f1', '3', '-f2', '-4'])
        parseInput.validate_campaign_or_event(a)
    
    def test_battle_sub_valid(self):
        a = parseInput.parse_arguments(['battle', '13-3', '4', '-f1', '3', '-s', '2'])
        self.assertEqual(a.sub, [2])
    
    def test_battle_default(self):
        a = parseInput.parse_arguments(['battle', '13-3', '4', '-f1', '3'])
        self.assertEqual(a.sub, 1)
        self.assertEqual(a.fleet2, None)
        self.assertFalse(a.heclp)
        self.assertFalse(a.timeout)

if __name__ == '__main__':
    u.main()