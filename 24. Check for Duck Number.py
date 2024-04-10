def is_duck(num):
    return '0' in str(num) and str(num)[0] != '0'

print("Is 102 a duck number?", is_duck(102))
