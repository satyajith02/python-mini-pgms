def is_harshad(num):
    sum_digits = sum(int(digit) for digit in str(num))
    return num % sum_digits == 0

print("Is 18 a harshad number?", is_harshad(18))
