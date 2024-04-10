def is_pronic(num):
    for i in range(num + 1):
        if i * (i + 1) == num:
            return True
    return False

print("Is 20 a pronic number?", is_pronic(20))
