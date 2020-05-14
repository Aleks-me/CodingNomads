'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

radius = 3.14
height = 5

# V = pi * r**2 * h
print("Cylinder volume:", 3.14 * radius**2 * height)

# S = 2*pi*r**2 + 2*pi*r*h = 2*pi*r*(r + h)
print("Cylinder surface area:", 2 * 3.14 * radius * (radius + height))
