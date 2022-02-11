import sys

#Euclidean Algo to calculate gcd
def calculate_gcd(n,m):

    if m == 0:
        return n
    
    return calculate_gcd(m,n%m)



def solution(input_list, gcd):

    res = []

    for i in range(1,len(input_list)):
        gcd = calculate_gcd(gcd,int(input_list[i]))
    
    for x in range(1,gcd+1):
        if gcd%x == 0:
            res.append(x)
    

    for i in range(0,len(res)):
        if i == len(res) - 1:
            print(res[i],end="")
        else:
            print(res[i],end=" ")

if __name__ == "__main__":
    ip_list = sys.argv[2:]
    gcd = int(ip_list[0])
    solution(ip_list, gcd)
