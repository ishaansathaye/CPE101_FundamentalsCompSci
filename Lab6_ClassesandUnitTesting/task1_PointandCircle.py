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

# def test_point_location():
#     assert point_location(point1, circle1) == 'These employees are both the same rank!', "Should be the same"
#     assert point_location(point1, circle1) == 'Dwight is senior in rank than Pam!', "Should be the Dwigth senior Pam"
#     assert point_location(point1, circle1) == 'Jim is senior in rank than Dwight!', "Should be Jim senior Dwight"
#     assert point_location(point1, circle1) == 'Jim is senior in rank than Pam!', "Should be Jim senior Pam"

# test_point_location()
# print("Everything Passed.")
# print()