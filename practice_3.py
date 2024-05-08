import math


def sin_taylor(x, n):
    result = 0
    sign = 1
    for i in range(n):
        term = sign * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        yield term
        result += term
        sign *= -1


def cos_taylor(x, n):
    result = 0
    sign = 1
    for i in range(n):
        term = sign * (x ** (2 * i)) / math.factorial(2 * i)
        yield term
        result += term
        sign *= -1


def exp_taylor(x, n):
    result = 0
    for i in range(n):
        term = (x**i) / math.factorial(i)
        yield term
        result += term


x = 1
n = 5

sin_series = list(sin_taylor(x, n))
cos_series = list(cos_taylor(x, n))
exp_series = list(exp_taylor(x, n))

sin_sum = sum(sin_series)
cos_sum = sum(cos_series)
exp_sum = sum(exp_series)

sin_difference = math.sin(x) - sin_sum
cos_difference = math.cos(x) - cos_sum
exp_difference = math.exp(x) - exp_sum

print(f"math.sin(x) - sin(x) = {sin_difference:.1e}")
print(f"math.cos(x) - cos(x) = {cos_difference:.1e}")
print(f"math.exp(x) - exp(x) = {exp_difference:.1e}")
