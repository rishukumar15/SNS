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

def get_solutions(a,b,m):

    gcd = calculate_gcd(a,m)

    solutions_list = []

    if b%gcd == 0:                  #Solution exists
        
        print("Y", end=" ")
        
        print(gcd, end=" ")         #No. of solutions = gcd

        alpha = a//gcd
        beta = b//gcd
        meu = m//gcd

        x0,y0 = extended_euclidean(alpha,meu)  #to get alpha inverse

        diff = 0

        x = (x0*beta)%meu

        for i in range(gcd):
            term = x + diff
            solutions_list.append(term)
            diff += meu
    else:
        print("N", end="")

    return solutions_list


if __name__ == "__main__":
    
    a = sys.argv[1]
    a = int(a)
    
    b = sys.argv[2]
    b = int(b)
    
    m = sys.argv[3]
    m = int(m)

    res = get_solutions(a,b,m)

    for i in range(0,len(res)):
        if i == len(res) - 1:
            print(res[i],end="")
        else:
            print(res[i],end=" ")