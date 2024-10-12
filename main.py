from mathematics.whoami import getname as math_name
from mathematics.numbers.whoami import getname as numbers_name
from mathematics.geometry.circle import circumference, area as circle_area
from mathematics.geometry.cube import surface_area, volume as cube_volume

print(math_name())
print(numbers_name())
print(circumference(radius=5))
print(circle_area(radius=5))
print(cube_volume(side=3))
