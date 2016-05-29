# You are computing the greatest common divisor ("gcd") of two positive
# integers called "a" and "b". The gcd can be computed recursively (or
# iteratively) using the following three rules: 
#
#       gcd(a,b) = a                    if a == b
#       gcd(a,b) = gcd(a-b,b)           if a > b
#       gcd(a,b) = gcd(a,b-a)           if a < b 

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    elif a < b:
        return gcd(a, b-a)

print (gcd(2, 6))
print (gcd(1362, 1407))
