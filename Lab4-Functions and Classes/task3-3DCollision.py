class Sphere:
    def __init__(self, x, y, z, radius) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.rad = radius
    def volumeCalc():
        pass

print()
print("This program will test if two objects are colliding.")
print()

print("Enter the details for the first sphere:")
sphere1 = Sphere()
sphere1.x = float(input("X-coord of the 1st sphere: "))
sphere1.y = float(input("Y-coord of the 1st sphere: "))
sphere1.z = float(input("Z-coord of the 1st sphere: "))
sphere1.rad = float(input("Radius of the 1st sphere: "))

print("Enter the details for the second sphere:")
sphere2 = Sphere()
sphere2.x = float(input("X-coord of the 2nd sphere: "))
sphere2.y = float(input("Y-coord of the 2nd sphere: "))
sphere2.z = float(input("Z-coord of the 2nd sphere: "))
sphere2.rad = float(input("Radius of the 2nd sphere: "))

