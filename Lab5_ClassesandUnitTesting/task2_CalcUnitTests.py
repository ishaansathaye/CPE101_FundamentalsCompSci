import unittest
import sys
sys.path.insert(0, "/Users/ishaansathaye/GitHub/CPE101_FundamentalsCompSci/Lab4_FunctionsandClasses")

from task1_FunctionCalc import add, subtract, mult, div

class TestFunctionCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,10), 12, "Should be 12")
        self.assertEqual(add(2,-10), -8, "Should be -8")

    def test_subtract(self):
        self.assertEqual(subtract(-6,-4), -2, "Should be -2")
        self.assertEqual(subtract(-10, 14), -24, "Should be -24")
    
    def test_mult(self):
        self.assertEqual(mult(2,-10), -20, "Should be -0")
        self.assertEqual(mult(-2,-11), 22, "Should be 22")

    def test_div(self):
        self.assertAlmostEqual(div(-15, 7), -2.14, 2, "Should be -2.14")
        self.assertAlmostEqual(div(-22,-13), 1.69, 2, "Should be 1.69")

if __name__ == "__main__":
    unittest.main()