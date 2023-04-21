import random
N = 9

bed = {a+1: random.randint(1, 10) for a in range (N)}

print(bed)