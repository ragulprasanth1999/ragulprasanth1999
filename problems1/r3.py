import math
i = int(input())
def is_prime(N):
    return N > 1 and all(N%2!=0 for j in range(2,int(math.sqrt(N+1))))
if is_prime(i):
    print(f"{i} is a prime number")
else:
    print(i," its not a prime number")