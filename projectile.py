# the equation
print('The equation: ', 'y = y\N{SUBSCRIPT ZERO} + x tan\N{GREEK CAPITAL LETTER THETA} - gx\N{SUPERSCRIPT TWO} / 2(v\N{SUBSCRIPT ZERO} cos\N{GREEK CAPITAL LETTER THETA})\N{SUPERSCRIPT TWO}')
print('y\N{SUBSCRIPT ZERO} = 1m')
print('x = 0.5m')
print('\N{GREEK CAPITAL LETTER THETA} = 80')
print('g = 9.81 m/s')
print('v\N{SUBSCRIPT ZERO} = 44 m/s')

import math
# this to import math into the code

height_of_barrel = 1
horizontal_distance = 0.5
angle = 80
gravity = 9.81
velocity = 44
theta = 80 * (math.pi/180)
print('theta =', theta)

x_tan_theta = horizontal_distance * (math.tan(theta))
print('x tan\N{GREEK CAPITAL LETTER THETA} =', x_tan_theta)

g_x_2 = gravity * pow(horizontal_distance, 2)
print('gx\N{SUPERSCRIPT TWO} =', g_x_2)

v0_cos_theta_2 = pow(44 * (math.cos(theta)), 2)
print('(v\N{SUBSCRIPT ZERO} cos\N{GREEK CAPITAL LETTER THETA})\N{SUPERSCRIPT TWO} =', v0_cos_theta_2)