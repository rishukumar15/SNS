import sys
import math

def is_prime_number(n):
    
    #check till square root of n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True

#Euclidean Algo to calculate gcd
def calculate_gcd(n,m):

    if m == 0:
        return n
    
    return calculate_gcd(m,n%m)

def phi_value_count(m):
    
    res = 1

    if is_prime_number(m):
        return m-res

    for i in range(2,m):

        g = calculate_gcd(i,m)
        if g == 1:
            res += 1
    
    return res


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


def get_RRSM_set(m):
    
    res = []
    res.append(1)
    for i in range(2,m):

        g = calculate_gcd(i,m)
        if g == 1:
            res.append(i)
    
    return res

def primitive_roots(m):

    
    
    val = phi_value_count(m)


    rrsm_set = get_RRSM_set(m)
   

    number_of_roots = phi_value_count(val)


    print(number_of_roots, end=" ")
    

    divisors_set = prime_factors(val)
    

    solutions = []
    
    
    for x in rrsm_set:

        flag = True

        for y in divisors_set:
            
            d = val//y

            if pow(x,d,m) == 1:
                flag = False
            
        if flag == True:
            solutions.append(x)


    for i in range(0,len(solutions)):
        if i == len(solutions) - 1:
            print(solutions[i], end="")
        else:
            print(solutions[i], end=" ")




if __name__ == "__main__":

    m = sys.argv[1]
    m = int(m)

    primitive_roots(m)