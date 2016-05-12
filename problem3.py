# Project Euler solutions by Girish 

# Problem 3 (Status : Success)

N = 600851475143
all_factors = []
prime_factors = []
starting_number = 2

def is_prime(a):
    return all(a % i for i in xrange(2, a))

while True:
    if N % starting_number == 0:
        all_factors.append(starting_number)
        N = N / starting_number
        if is_prime(N):
            all_factors.append(N)
            break
    else:
        starting_number += 1

print max(all_factors)

# Output : 6857