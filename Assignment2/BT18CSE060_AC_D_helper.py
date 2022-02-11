import math



def is_prime_number(n):
    
    #check till square root of n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True





def calculate_gcd(n,m):

    if m == 0:
        return n
    
    return calculate_gcd(m,n%m)





def extended_euclidean(a,b):
    
    #Base Case
    if b == 0:
        return 1,0
    
    x1,y1 = extended_euclidean(b,a%b)

    y = x1 - (a//b) * y1
    x = y1

    return x,y





def phi_value_count(m):
    
    res = 1

    if is_prime_number(m):
        return m-res

    for i in range(2,m):

        g = calculate_gcd(i,m)
        if g == 1:
            res += 1
    
    return res




def multiplicative_inverse(a,m):                #to get multiplicative inverse of a under modulo m

    if calculate_gcd(a,m) == 1:

        x,y = extended_euclidean(a,m)
        inv = (x+m)%m
        return inv
    else:
        return -1





def prime_factors(n):                       #to get prime factors of n
     
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






def primitive_roots(m):

    val = phi_value_count(m)

    divisors_set = prime_factors(val)
    
    for x in range(1, m):       #RRSM set of m(prime) contains value from 1 to m-1

        flag = True

        for y in divisors_set:
            
            d = val//y

            if pow(x,d,m) == 1:
                flag = False
            
        if flag == True:
            return y                #return the first primitive root from the roots set
    
    return -1