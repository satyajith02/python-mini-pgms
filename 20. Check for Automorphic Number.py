def is_automorphic(num):
    square = num ** 2
    return str(square).endswith(str(num))

print("Is 25 an automorphic number?", is_automorphic(25))
