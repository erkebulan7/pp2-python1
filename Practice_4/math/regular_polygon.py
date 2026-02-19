import math

n = int(input())
side = float(input())

angle = math.pi / n
tan_value = math.tan(angle)

area = (n * side * side) / (4 * tan_value)

print(area)
