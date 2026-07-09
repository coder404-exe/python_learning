import math
def circle(radius):
    area=math.pi *radius*radius
    circumference=2*math.pi*radius
    return area,circumference
radius=7
print(circle(radius))