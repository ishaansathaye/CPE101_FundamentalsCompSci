import math

class Point:
    def __init__(self) -> None:
        self.x = float(input("Enter x coordinate of point: "))
        self.y = float(input("Enter y coordinate of point: "))

class Circle:
    def __init__(self) -> None:
        self.x = float(input("Enter the x-coord center of circle: "))
        self.y = float(input("Enter the y-coord center of circle: "))
        self.radius = float(input("Enter the radius of the circle: "))

def point_location(point, circle):
    distance = math.sqrt(((point.x - circle.x)**2) + ((point.y - circle.y)**2))
    if distance == circle.radius:
        return "On Circle!"
    elif distance < circle.radius:
        return "Inside Circle!"
    else:
        return "Outside Circle!"

print()
point1 = Point()
print()
circle1 = Circle()
print()
print(point_location(point1, circle1))
print()

'''Manual Tests'''
# def test_point_location():
#     circle1.radius = 6
#     assert point_location(point1, circle1) == 'Inside Circle!', "Should be inside the circle since distance less than radius (6)"
#     circle1.radius = 2
#     assert point_location(point1, circle1) == 'Outside Circle!', "Should be outside the circle since distance greater than radius (2)"
#     circle1.radius = 5
#     assert point_location(point1, circle1) == 'On Circle!', "Should be on the circle since distance equals radius (5)"

# test_point_location()
# print("Everything Passed.")
# print()
