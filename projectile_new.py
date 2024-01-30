import math
# this to import math into the code
# import usually goes on the first line

# yo = height of barrel
# x = horizontal distance travelled
# angle
# g = gravity
# v = velocity
# theta = angle * (pi/180)
# y is height of projectile

y0 = 1
x = 0.5
angle = 80
g = 9.81
v = 44
theta = 80 * (math.pi/180)

y = y0 + x * math.tan(theta) - (g * x**2) / (2 * (v * math.cos(theta))**2)
print('y =', y)
print('The height of the projectile rounded to 2 decimal place is', str(round(y, 2)), 'm')
# used the rounding function to round the answer to 2 decimal place

# the equation without working out the theta beforehand
y = y0 + x * math.tan(80 * (math.pi/180)) - (g * x**2) / (2 * (v * math.cos(80 * (math.pi/180)))**2)
print(y)
