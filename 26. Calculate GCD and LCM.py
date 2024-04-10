def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print("GCD of 12 and 18:", gcd(12, 18))
print("LCM of 12 and 18:", lcm(12, 18))
