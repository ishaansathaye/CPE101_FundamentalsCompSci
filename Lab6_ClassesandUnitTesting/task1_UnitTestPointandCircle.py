import unittest
from task1_PointandCircle 

class TestEmployeeClass(unittest.TestCase):

    def setUp(self):
        self.employee1 = employee("Michael", 45, 12345)
        self.employee2 = employee("Dwight", 40, 23456)
        self.employee3 = employee("Pam", 30, 34567)
        self.employee4 = employee("Jim", 35, 12345)
        
    def test_point_location1(self):
        self.assertEqual(self.employee1.is_higher_rank(self.employee4), 
        "These employees are both the same rank!",
        "Should be same")

    def test_point_location2(self):
        self.assertEqual(self.employee3.is_higher_rank(self.employee2), 
        "Dwight is senior in rank than Pam!",
        "Should be Dwight higher than Pam")

    def test_point_location4(self):
        self.assertEqual(self.employee4.is_higher_rank(self.employee2), 
        "Jim is senior in rank than Dwight!",
        "Should be Jim senior to Dwight")
    
    def test_point_location4(self):
        self.assertEqual(self.employee4.is_higher_rank(self.employee3), 
        "Jim is senior in rank than Pam!",
        "Should be Jim senior to Pam")

if __name__ == "__main__":
    unittest.main()