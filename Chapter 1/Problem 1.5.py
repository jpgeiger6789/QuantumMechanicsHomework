import math
import statistics

"""

"""



"""
Problem 1.4 (for reference)
a)
It really feels like p(x) should be a constant 1/xmax since there is a 1-to-1 mapping between the angle and the
position and p(θ) is a constant = 1/pi
However we do need to prove this somehow  (turns out to be false?)
p(θ) = 1 / pi
x(θ) = cos(θ)
θ = acos(x)
P(θ) = S p(θ) dθ | evaluated from θ to θ + dθ
P(θ) = θ / pi | θ to θ + dθ
P(θ) = (θ + dθ) / pi - θ / pi
P(θ) = dθ / pi
    dx/dθ = -sin(θ)
    dθ = - dx / sin(θ) 
    dθ = - dx / sin(acos(x))
        sin(acos(x)) = sqrt(1-x^2)
        this is derived from sin(θ)^2+cos(θ)^2=1
        sin(acos(x))^2 + cos(acos(x))^2 = 1
        sin(acos(x))^2 = 1 - x^2
    dθ = - dx / sqrt(1-x^2) 
P(x) =  -dx / [pi*sqrt(1-x^2)]
Total probability = integral of P(x) from x = -1 to 1
S -dx / [pi * sqrt(1-x^2)] = asin(x)/pi <<wolfram-alpha

asin(1)/pi - asin(-1)/pi  this does sum to 1!
P(x) = asin(x)/pi
p(x) = 1/[pi*sqrt(1-x^2)]

<x> = S x*p(x) | -1 to 1
    S x / [pi * sqrt(1-x^2)] * dx
    h = (1-x^2)
    dh = -2x * dx
    dx = dh / -2x
    S -dh / [2 * pi * sqrt(h)]
    = -sqrt(h) / pi
    = -sqrt(1-x^2) / pi | -1 to 1
    = 0  <<this makes sense
<x^2> = S x^2 * p(x) | -1 to 1
    = [asin(x) - x * sqrt(1-x^2)] / (2 * pi) <<wolfram-alpha | -1 to 1
    = pi (I cheated and used python)
variance = <x^2> - <x> ^ 2 = pi
std dev = sqrt(variance) = sqrt(pi)
"""

def f(x):
    return((math.asin(x) - x * math.sqrt(1 - x ** 2) / (2 * math.pi)))


n = [p(i/100) for i in range(-99, 99, 1)]
avg = sum(n) / len(n)
sqrs = [i ** 2 for i in n]
variances = [(i - avg) ** 2 for i in n]
variance = statistics.mean(variances)
avgOfSquares = statistics.mean(sqrs)
altvariance = avgOfSquares - avg ** 2

print(f"sum of squares is {sum(sqrs)}")
print(f"average of squares is {statistics.mean(sqrs)}")
print(f"average value is {avg}")

print(f"the variance as calculated by the average of the variances is {variance}")
print(f"the standard deviation as calculated by the square root of the variance is {variance ** .5}")
print(f"the variance as calculated by the average of the squares minus the square of the average is {altvariance}")
print(f"the standard deviation as calculated by the square root of this variance is {altvariance ** .5}")

print(f"the mean is {statistics.mean(n)}")
print(f"the bias-corrected variance is {statistics.variance(n)}")
print(f"the bias-corrected standard deviation is {statistics.stdev(n)}")
print(f"the uncorrected variance is {statistics.pvariance(n)}")
print(f"the uncorrected standard deviation is {statistics.pstdev(n)}")