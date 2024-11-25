import math
import cmath

print(f"Value of pi: {math.pi}")
print(f"Value pf e: {math.e}")

number = 16
print(f"Square root of {number}: {math.sqrt(number)}")

angle = math.radians(90)
print(f"Sin(90°): {math.sin(angle)}")


value = 10
print(f"Natural log of {value}: {math.log(value)}")
print(f"Base-10 log of {value}: {math.log10(value)}")


z = 3 + 4j
print(f"Complex number: {z}")

print(f"Magnitude: {abs(z)}")
print(f"Phase (angle in radians): {cmath.phase(z)}")

polar = cmath.polar(z)
print(f"Polar coordinates (r, θ): {polar}")

print(f"Cosine of {z}: {cmath.cos(z)}")

# Area of a Circle
radius = 34
area = math.pi * radius ** 2  # Using the correct formula
print(f"Area of a circle with radius {radius}: {area}")

# Cosine of a 45° Angle
angle = math.radians(45)  # Converting to radians
print(f"Cosine of 45°: {math.cos(angle)}")

# Logarithm Base 10 of 20
print(f"Logarithm base 10 of 20: {math.log10(20)}")

# Square Root of -16
print(f"Square root of -16: {cmath.sqrt(-16)}")
