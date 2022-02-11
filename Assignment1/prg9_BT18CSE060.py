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

def phi_value_count(n):
    
    result = n

    p = 2 

    while p * p <= n :


        if n % p == 0 : 


            while n % p == 0 :

                n = int(n / p)

            result -= int(result / p)

        p += 1;
 

    if n > 1 :

        result -= int(result / n)

    return result




def calculate_divisors(n):

    st = set()

    for i in range(1,int(math.sqrt(n))+1):

        if n%i == 0:
            st.add(i)
            st.add(n//i)

    div_lst = list(st)
    
    div_lst.sort()
    
    return div_lst

def order(a,m):

    val = phi_value_count(m)

    divs = calculate_divisors(val)

    for x in divs:

        if pow(a,x,m) == 1:
            return x




if __name__ == "__main__":
    
    a = sys.argv[1]
    a = int(a)

    m = sys.argv[2]
    m = int(m)

    h = order(a,m)
    
    print(h, end="")