import unittest
from test import calculate_average

class TestAverageCalculator(unittest.TestCase):

    def test_calculate_average_valid_input(self):
        numbers = [1, 2, 3, 4, 5]
        result = calculate_average(numbers)
        self.assertAlmostEqual(result, 3.0, places=2)

    def test_calculate_average_empty_input(self):
        numbers = []
        with self.assertRaises(ValueError):
            calculate_average(numbers)

    def test_calculate_average_invalid_input(self):
        numbers = [1, 2, 'a', 4, 5]
        with self.assertRaises(ValueError):
            calculate_average(numbers)

if __name__ == '__main__':
    unittest.main()