import math

class Sphere:
    def __init__(self, position):
        self.x = float(input("X-coord of the " + position + " sphere: "))
        self.y = float(input("Y-coord of the " + position + " sphere: "))
        self.z = float(input("Z-coord of the " + position + " sphere: "))
        self.rad = float(input("Radius of the " + position + " sphere: "))
    def volumeCalc(self):
        return round((4/3)*(math.pi)*(pow(self.rad, 3)), 2)
    def collision(self, s2x, s2y, s2z, s2rad):
        distance = round(math.sqrt(((self.x-s2x)**2)+((self.y-s2y)**2)+((self.z-s2z)**2)), 2)
        if distance <= (self.rad + s2rad):
            return True
        else:
            return False

print()
print("This program will test if two objects are colliding.")
print()

print("Enter the details for the 1st sphere:")
sphere1 = Sphere("1st")

print()
print("Enter the details for the 2nd sphere:")
sphere2 = Sphere("2nd")

print()
if sphere1.volumeCalc() == sphere2.volumeCalc():
    print("The 2 Spheres are IDENTICAL with a Volume of", sphere2.volumeCalc())
elif sphere1.collision(sphere2.x, sphere2.y, sphere2.z, sphere2.rad) == True:
    print("The Spheres COLLIDE!")
else:
    print("The Spheres do not collide!")
    if sphere1.volumeCalc() > sphere2.volumeCalc():
        multiplier = round(sphere1.volumeCalc() / sphere2.volumeCalc(), 2)
        print("Sphere 1 is", str(multiplier), "times bigger than Sphere 2!")
    else:
        multiplier = sphere2.volumeCalc() / sphere1.volumeCalc()
        print("Sphere 2 is", str(multiplier), "times bigger than Sphere 1!")

print()