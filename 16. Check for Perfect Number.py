def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

print("Is 28 a perfect number?", is_perfect(28))
