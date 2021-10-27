import unittest
import task1_PointandCircle as pc

class TestEmployeeClass(unittest.TestCase):
    '''Automated Tests'''
    def test_point_location1(self):
        pc.circle1.radius = 6
        assert pc.point_location(pc.point1, pc.circle1) == 'Inside Circle!', "Should be inside the circle since distance less than radius (6)"

    def test_point_location2(self):
        pc.circle1.radius = 2
        assert pc.point_location(pc.point1, pc.circle1) == 'Outside Circle!', "Should be outside the circle since distance greater than radius (2)"

    def test_point_location4(self):
        pc.circle1.radius = 5
        assert pc.point_location(pc.point1, pc.circle1) == 'On Circle!', "Should be on the circle since distance equals radius (5)"

if __name__ == "__main__":
    unittest.main()