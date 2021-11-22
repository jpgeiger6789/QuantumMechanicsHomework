import statistics
import mpmath

"""
a)
Since the probability is equal everywhere, the probability density function is a constant.  Since it sums to 1 and is
distributed across an interval of length pi, the value of the constant is:
p(θ) = 1 / pi
x(θ) = cos(θ)
cos(θ) = sin(θ + pi /2)
x(θ) = sin(θ + pi / 2)
θ = asin(x) - pi / 2
P(θ) = S p(θ) dθ | evaluated from θ to θ + dθ
P(θ) = θ / pi | θ to θ + dθ
P(θ) = (θ + dθ) / pi - θ / pi = dθ / pi
    dx/dθ = -sin(θ)
    dθ = - dx / sin(θ) 
    dθ = - dx / sin(acos(x))
    dθ = - dx / sqrt(1-x^2)
P(x) = dx/pi*sqrt(1-x^2)
P(x) = dx/pi*sqrt[(1+x)(1-x)]
P(x) = S p(x) | evaluated from x to x + dx
S p(x) = x/pi*sqrt(1-x^2) where (x + dx)^2 ~ x^2
p(x) = d/dx [x/pi*sqrt(1-x^2)]
    g = pi*sqrt(1-x^2)
    g = pi*sqrt(h)
    h = 1-x^2
    dh/dx = -2x
    dg/dh = pi/2h
    d/dx[x/g] = 1/g*dx -x/g^2 * dg/dx
    dg/dx = dg/dh * dh/dx = pi/[2(1-x^2)] * -2x = -2*pi*x/[2*(1-x^2)]
    d/dx[x/(pi * sqrt{1-x^2})] = [1/(pi*sqrt{1-x^2})] - [x/{pi*sqrt(1-x^2)}^2] * [pi/(2*{1-x^2})]
p(x) = = [1/(pi*sqrt{1-x^2})] - [x/{pi*sqrt(1-x^2)}^2] * [pi/(2*{1-x^2})]


"""








mpmath.mp.dps = 25

strPi = str(mpmath.mp.pi)

print(f"pi is {strPi}")
print(f"len pi is {len(strPi)}")

piDigits = [int(i) for i in strPi if "0" <= i <= "9"]
for i in range(10):
    numFound = piDigits.count(i)
    print(f"the probability of finding the digit {i} in the first 25 digits of pi is {numFound / 25}")
piSorted = piDigits[:]
piSorted.sort()
print(f"I calculate the median digit to be {piSorted[12]}")
print(f"the median digit is {statistics.median(piDigits)}")
print(f"the average value of the first 25 digits of pi is {statistics.mean(piDigits)}")

n = piDigits
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