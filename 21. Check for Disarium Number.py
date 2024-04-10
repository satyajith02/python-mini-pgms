def is_disarium(num):
    temp = num
    sum = 0
    n = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        n -= 1
        temp //= 10
    return sum == num

print("Is 175 a disarium number?", is_disarium(175))
