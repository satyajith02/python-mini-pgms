def factorial_digit(n):
    factorial_sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        factorial_sum += factorial(digit)
        temp //= 10
    return factorial_sum == n

print("Is 145 a strong number?", factorial_digit(145))
