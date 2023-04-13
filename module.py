import math
import statistics

import mymodule
from mymodule import x,y

mymodule.Shule("eMobilis Mobile Technology")
print("Addition ", mymodule.x + mymodule.y)
print("Subtraction ", mymodule.y - mymodule.x)
print("Multiplication ", mymodule.x * mymodule.y)
print("Division ", mymodule.y / mymodule.x)
print(x+y)

# This is inbuilt modules function
print("The square root is ",math.sqrt(25))
dataset = [6, 2, 14, 78, 4, 7, 1, 87]
x = statistics.mean(dataset)
y = statistics.median(dataset)
m = statistics.geometric_mean(dataset)
p = statistics.harmonic_mean(dataset)
z = statistics.mode(dataset)
l = statistics.variance(dataset)
print("Mean is ", x)
print("Median is ", y)
print("Geometric median is ", m)
print("Harmonic mean is ", p)
print("Mode is ", z)
print("Variance is ", l)
