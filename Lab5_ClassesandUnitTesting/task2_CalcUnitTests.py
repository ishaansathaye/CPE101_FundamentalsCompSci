import Lab4_FunctionsandClasses.task1_FunctionCalc as FunctionCalc

import unittest

class TestFunctionCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(FunctionCalc.add(2,10), 12, "Should be 12")
        self.assertEqual(FunctionCalc.add(2,-10), -8, "Should be 12")

    def test_subtract(self):
        pass
    
    def test_mult(self):
        pass

    def test_div(self):
        pass

if __name__ == "__main__":
    unittest.main()