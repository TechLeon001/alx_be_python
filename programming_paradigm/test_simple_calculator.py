import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class."""

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test zero
        self.assertEqual(self.calc.add(0, 5), 5)
        # Test commutative property
        self.assertEqual(self.calc.add(3, 2), self.calc.add(2, 3))
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction(self):
        """Test the subtract method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        # Test order matters
        self.assertEqual(self.calc.subtract(3, 5), -2)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    def test_multiplication(self):
        """Test the multiply method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        # Test commutative property
        self.assertEqual(self.calc.multiply(3, 2), self.calc.multiply(2, 3))
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)
        # Test identity property
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_division(self):
        """Test the divide method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test floating point result
        self.assertAlmostEqual(self.calc.divide(1, 2), 0.5, places=7)
        # Test division by 1
        self.assertEqual(self.calc.divide(5, 1), 5)
        # Test division of negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test floating point division
        self.assertAlmostEqual(self.calc.divide(0.3, 0.1), 3.0, places=7)

    def test_division_edge_cases(self):
        """Additional edge cases for division."""
        # Test 0 divided by non-zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Test very small numbers
        self.assertAlmostEqual(self.calc.divide(1e-10, 2), 5e-11, places=20)
        # Test very large numbers
        self.assertAlmostEqual(self.calc.divide(1e10, 2), 5e9, places=7)

if __name__ == '__main__':
    unittest.main()