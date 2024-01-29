import math
# this to import math into the code

# the equation
print('The equation: ', 'y = y\N{SUBSCRIPT ZERO} + x tan\N{GREEK CAPITAL LETTER THETA} - gx\N{SUPERSCRIPT TWO} / 2(v\N{SUBSCRIPT ZERO} cos\N{GREEK CAPITAL LETTER THETA})\N{SUPERSCRIPT TWO}')
print('y\N{SUBSCRIPT ZERO} = 1m')
print('x = 0.5m')
print('angle = 80')
print('g = 9.81 m/s')
print('v\N{SUBSCRIPT ZERO} = 44 m/s')


height_of_barrel = 1
horizontal_distance = 0.5
angle = 80
gravity = 9.81
velocity = 44
theta = 80 * (math.pi/180)
print('theta =', theta)
# to convert angles to radian the question is the angle * pi/180

# Using the BIDMAS rule, first work out the brackets

v0_cos_theta = 44 * (math.cos(theta))
print('v\N{SUBSCRIPT ZERO}cos\N{GREEK CAPITAL LETTER THETA} =', v0_cos_theta)
# using the subscripts to print the answers to keep track of which part of the equation I've calculated

# then work out the indices
v0_cos_theta_2 = pow(v0_cos_theta, 2)
print('(v\N{SUBSCRIPT ZERO}cos\N{GREEK CAPITAL LETTER THETA})\N{SUPERSCRIPT TWO} =', v0_cos_theta_2)

# multiplication next
two_v0_cos_theta_2 = v0_cos_theta_2 * 2
print('2(v\N{SUBSCRIPT ZERO}cos\N{GREEK CAPITAL LETTER THETA})\N{SUPERSCRIPT TWO} =', two_v0_cos_theta_2)

g_x_2 = gravity * pow(horizontal_distance, 2)
print('gx\N{SUPERSCRIPT TWO} =', g_x_2)

x_tan_theta = horizontal_distance * (math.tan(theta))
print('x tan\N{GREEK CAPITAL LETTER THETA} =', x_tan_theta)

# then worked out the division
gx_v0_cos = g_x_2 / two_v0_cos_theta_2
print('gx\N{SUPERSCRIPT TWO} / 2(v\N{SUBSCRIPT ZERO} cos\N{GREEK CAPITAL LETTER THETA})\N{SUPERSCRIPT TWO} =', gx_v0_cos)

# combine the worked out answers to find the y value
y = height_of_barrel + x_tan_theta - gx_v0_cos
print('y =', y)

print('The height of the projectile rounded to 2 decimal place is', str(round(y, 2)), 'm')
# used the rounding function to round the answer to 2 decimal place

