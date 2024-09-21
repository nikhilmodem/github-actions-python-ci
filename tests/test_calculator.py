import unittest
from src.calculator import add, subtract, divide 

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 10), 0)
        self.assertEqual(subtract(-1, -1), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, -2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(10, 0), "Error: Division by zero")  # Test for division by zero

if __name__ == '__main__':
    unittest.main()
