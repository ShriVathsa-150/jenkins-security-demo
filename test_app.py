
import unittest
from app import add, divide

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 20), 30)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_zero(self):
        self.assertEqual(divide(10, 0),
                         "Cannot divide by zero")

if __name__ == "__main__":
    unittest.main()
