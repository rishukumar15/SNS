import sys

#Euclidean Algo to calculate gcd
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

def multiplicative_inverse(a,m):

    if calculate_gcd(a,m) == 1:
        print("Y", end=" ")

        x,y = extended_euclidean(a,m)
        inv = (x+m)%m
        print(inv, end="")
    else:
        print("N", end="")

if __name__ == "__main__":
    
    a = sys.argv[1]
    a = int(a)
    
    m = sys.argv[2]
    m = int(m)
    
    multiplicative_inverse(a,m)