import sys
import math

#Euclidean Algo to calculate gcd
def calculate_gcd(n,m):

    if m == 0:
        return n
    
    return calculate_gcd(m,n%m)

def is_prime_number(n):
    
    #check till square root of n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        
    return True

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





def solution(a,x,n):

    equations = []
    equations.append(f"{a}^{x}(mod{n})")

    #compute phi(n)
    phi_val = phi_value_count(n)

    #represnt x as x = phi_val*q + r
    #reduced to a^r(modn)
    q = x//phi_val
    r = x%phi_val

    equations.append(f"{a}^({q}*{phi_val}+{r})(mod{n})")
    equations.append(f"({a}^{phi_val}(mod{n}))^{q} . {a}^{r}(mod{n})")
    equations.append(f"({a}^Φ({n})(mod{n}))^{q} . {a}^{r}(mod{n})")
    equations.append(f"(1)^{q} . {a}^{r}(mod{n})")
    equations.append(f"1 . {a}^{r}(mod{n})")

    p = a**r

    equations.append(f"1 . {p}(mod{n})")

    ans = p%n
    equations.append(f"1 . {ans}")



    print(ans, end="")

    """
    for x in equations:             #commented lines for equations printing
        print(x,end=" ")

    """

if __name__ == "__main__":
    
    a = sys.argv[1]
    a = int(a)
    
    x = sys.argv[2]
    x = int(x)
    
    n = sys.argv[3]
    n = int(n)

    solution(a,x,n)