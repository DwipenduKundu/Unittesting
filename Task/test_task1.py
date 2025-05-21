import unittest
import task1


class TestIPLAnalysis(unittest.TestCase):
    test_path = './data/test_matches.csv'

    def test_matches_per_year(self):
        result = task1.start1(self.test_path)
        expected = ['2015', '2016'], [2, 3]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
