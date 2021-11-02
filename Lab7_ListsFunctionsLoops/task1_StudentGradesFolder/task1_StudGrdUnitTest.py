import unittest
from task1_StudentGrades import calculate_average as ca

class TestCalcAverageFunc(unittest.TestCase):
    '''Automated Tests'''
    def test_average1(self):
        gradesList = [90, 100, 20, 45, 67]
        assert ca(gradesList) == 64.4, "Average should be 64.4"

    def test_average2(self):
        gradesList = [67, 48, 78, 99, 69]
        assert ca(gradesList) == 72.2, "Average should be 72.2"

    def test_average3(self):
        gradesList = [97, 87, 65, 84, 93]
        assert ca(gradesList) == 85.2, "Average should be 85.2"

if __name__ == "__main__":
    unittest.main()