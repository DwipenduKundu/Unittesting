import unittest
import task2


class TestIPLAnalysis(unittest.TestCase):
    test_path = './data/test_matches.csv'

    def test_matches_won_by_team(self):
        result = dict(task2.start2(self.test_path))
        expected = {
            '2015': {'Kolkata Knight Riders': 1, 'Chennai Super Kings': 1},
            '2016': {'Rising Pune Supergiants': 1, 'Royal Challengers Bangalore': 1, 'Kolkata Knight Riders': 1}
        }

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
