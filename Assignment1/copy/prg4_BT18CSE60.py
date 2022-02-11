import sys

#Euclidean Algo to calculate gcd
def calculate_gcd(n,m):

    if m == 0:
        return n
    
    return calculate_gcd(m,n%m)

def get_RRSM_set(m):

    res = []
    res.append(1)
    for i in range(2,m):

        g = calculate_gcd(i,m)
        if g == 1:
            res.append(i)
    
    return res

if __name__ == "__main__":

    m = sys.argv[1]
    m = int(m)
    ans = get_RRSM_set(m)
    for x in ans:
        print(x, end=" ")
    
    nums = len(ans)

    print(nums, end="")