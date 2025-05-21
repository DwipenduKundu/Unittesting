import unittest
import task3


class TestIPLAnalysis(unittest.TestCase):
    match_test_path = './data/test_matches.csv'
    deliveries_test_path = './data/test_deliveries_lessdata.csv'

    def test_extra_runs_conceded_2016(self):
        result_team, result_run = task3.start3(
            self.deliveries_test_path, self.match_test_path)
        expected = [['Rising Pune Supergiants', 'Mumbai Indians', 'Sunrisers Hyderabad',
                     'Royal Challengers Bangalore', 'Kolkata Knight Riders'],
                    [3, 0, 2, 5, 1]
                    ]
        result = [list(result_team)]+[list(result_run)]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
