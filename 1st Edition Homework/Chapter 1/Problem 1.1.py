import statistics

n = [14,15]+[16]*3+[22,24]*2+[25]*5
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

print(f"standard deviation is {statistics.stdev(n)}")