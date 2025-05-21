import unittest
import task4


class TestIPLAnalysis(unittest.TestCase):
    match_test_path = './data/test_matches.csv'
    deliveries_test_path = './data/test_deliveries_lessdata.csv'

    def test_top_economical_bowlers_2015(self):
        result_name, result_economy = task4.start4(
            self.deliveries_test_path, self.match_test_path)
        result = [list(result_name)]+[list(result_economy)]
        expected = [['A Nehra', 'UT Yadav', 'R Vinay Kumar', 'MM Sharma', 'M Morkel', 'SL Malinga', 'JA Morkel', 'NM Coulter-Nile'],
                    [0, 3, 3, 3, 12, 12, 12, 12]
                    ]
        self.assertEqual(result, expected)
        


if __name__ == '__main__':
    unittest.main()
