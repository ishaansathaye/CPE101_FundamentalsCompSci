import unittest
from task1_HeartRate import calculate_average_heart_rates as calcAverage

class TestEmployeeClass(unittest.TestCase):
        
    def test_calcAverageHeartRate1(self):
        heart_rate = [[ 72, 75, 71, 73]]
        self.assertAlmostEquals(calcAverage(heart_rate), [72.75], 2, "Should be 72.75")

    def test_calcAverageHeartRate2(self):
        heart_rate = [[ 91, 90, 94, 93]]
        self.assertAlmostEquals(calcAverage(heart_rate), [92.0], 2, "Should be 92")

    def test_calcAverageHeartRate3(self):
        heart_rate = [[ 130, 135, 139, 142]]
        self.assertAlmostEquals(calcAverage(heart_rate), [136.5], 2, "Should be 136.5")
    
    def test_calcAverageHeartRate4(self):
        heart_rate = [[ 120, 118, 110, 105, 100, 98]]
        self.assertAlmostEquals(calcAverage(heart_rate), [108.5], 2, "Should be 108.5")

if __name__ == "__main__":
    unittest.main()