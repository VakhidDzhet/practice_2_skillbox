import math


def cartesian_to_polar(x, y):
    radius = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)
    return radius, phi


x, y = map(float, input("Enter the Cartesian coordinates as x;y: ").split(";"))

radius, phi = cartesian_to_polar(x, y)

print(f"Polar radius: radius={radius:.3f}")
print(f"Polar angle: phi={phi:.3f}")
