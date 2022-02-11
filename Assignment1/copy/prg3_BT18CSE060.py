import sys
import math

def is_prime_number(n):

    #check till square root of n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True

def prime_factors(n):

    i = 3
    pFactors = []
    while n%2==0:
        pFactors.append(2)
        n=n//2
    while i*i<=n:
        while n%i==0:
            pFactors.append(i)
            n=n//i        
        i+=2
    if n>2:
        pFactors.append(n)

    return pFactors
    


if __name__ == "__main__":
    n = sys.argv[1]
    n = int(n)
    res = prime_factors(n)
    for i in range(0,len(res)):
        if i == len(res) - 1:
            print(res[i],end="")
        else:
            print(res[i],end=" ")
    

