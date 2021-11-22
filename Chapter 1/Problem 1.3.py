import statistics
import mpmath

"""
a)
Since the probability is equal everywhere, the probability density function is a constant.  Since it sums to 1 and is
distributed across an interval of length pi, the value of the constant is:
p(θ) = 1 / pi
The graph will be:
0 from -pi / 2 to 0
1 / pi from 0 to pi
0 from pi to 3 * pi / 2
b)
the average must be pi / 2
The sum of the value is the integral of the probability function from 0 to pi and must be 1 (probability must sum to 1)
Sum(x) = Sp(θ) = x / pi + C | evaluated from 0 to pi
Sum(x) = pi / pi  - 0 / pi  = 1 (as expected)
The average of the value is the integral of the probability function times x, evaluated from 0 to pi, and should be pi / 2
Avg(x) = Sx*p(θ) = x^2/2 * pi + c | evaluated from 0 to pi
Avg(x) = pi ^ 2 / 2 * pi - 0^2 / 2 * pi = pi / 2 (as expected)
Avg(x^2) = S x^2 * p(θ) = x ^ 3 / 3 * pi | evaluated from 0 to pi
Avg(x^2) = pi ^ 3 / 3 * pi - 0 ^ 3 / 3 * pi = pi ^ 2 / 3
variance = Avg(x^2) - Avg(x)^2 = pi ^ 2 / 3 - pi ^2 / 4 = pi^2 / 12
sigma = sqrt(variance) = sqrt(pi ^ 2 /  12) = pi / sqrt(12)
c)
Avg(sin(x)) = S sin(x) * p(θ) = -cos(x) / pi | evaluated from 0 to pi
Avg(sin(x)) = -cos(pi) / pi - cos(0) / pi = 1 / pi - 1 / pi = 0 (as expected)
Avg(cos(x) = S cos(x) * p(θ) = sin(x) / pi | evaluated from 0 to pi
Avg(cos(x)) = sin(pi) / pi - sin(0) / pi = 0 - 0 = 0 (as expected)
Avg(cos^2(x)) = S cos^2(x) * p(θ) = S (1 + cos(2 * x)) / 2 * p(θ)
   = S 1/pi + cos(2 * x) / 2 * pi
   = x/pi + sin(2 * x) / 4 * pi | evaluated from 0 to pi
   = pi / pi + sin(2pi) / 4pi - 0/pi + sin(0)/4*pi
   = 1 (not sure what I expected tbh)
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