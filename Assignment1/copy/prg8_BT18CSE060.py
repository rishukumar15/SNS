import sys

#Euclidean Algo to calculate gcd
def calculate_gcd(n,m):

    if m == 0:
        return n
    
    return calculate_gcd(m,n%m)


def extended_euclidean(a,b):        #to calculate multiplicative inverse under modulo
    
    #Base Case
    if b == 0:
        return 1,0
    
    x1,y1 = extended_euclidean(b,a%b)

    y = x1 - (a//b) * y1
    x = y1

    return x,y

def is_CRT_applicable(m_list):      #check whether (mi,mj) = 1 for all i,j and i != j for CRT

    ans = True

    for i in range(len(m_list)):

        a = m_list[i]

        for j in range(i+1,len(m_list)):

            b = m_list[j]
            if calculate_gcd(a,b) != 1:
                ans = False
                return ans
            
    
    return ans


def convert_into_CRT_form(equations):

    new_equations = []

    for i in range(len(equations)):
        
        eq = equations[i]

        a = eq[0]
        b = eq[1]
        m = eq[2]
        a_inv,y = extended_euclidean(a,m)

        a_inv = (a_inv+m)%m

        temp = []
        temp.append(1)
        temp.append(b*a_inv)
        temp.append(m)

        new_equations.append(temp)

    return new_equations


def is_individual_solutions_exist(equations):
    
    ans = True

    for i in range(len(equations)):
        
        eq = equations[i]

        a = eq[0]
        b = eq[1]
        m = eq[2]
        g = calculate_gcd(a,m)
        if g != 1 or b%g != 0:
            ans = False
            return ans

    return ans



def apply_CRT(eqs, m_list):

    if is_CRT_applicable(m_list) and is_individual_solutions_exist(eqs):

        print("Y", end=" ")

        equations = convert_into_CRT_form(eqs)

        #compute M
        M = 1
        for eq in equations:
            M = M*eq[2]

        #apply crt formula
        b_list = []
        a_list = []
        for eq in equations:

            #(M/Mj) invers mod mj
            inv,y = extended_euclidean(M//eq[2],eq[2])
            a_list.append(eq[1])
            inv = (inv+eq[2])%eq[2]
            b_list.append(inv)

        ans = 0

        for i in range(len(equations)):

            m = m_list[i]
            a = a_list[i]
            b = b_list[i]

            ans += (M//m)*a*b

        print(ans%M, end="")

    else:

        print("N", end="")

if __name__ == "__main__":

    ip_list = sys.argv[2:] 

    equations = []
    m_list = []

    #get the equations
    for i in range(0,len(ip_list),3):

        a = int(ip_list[i])
        b = int(ip_list[i+1])
        m = int(ip_list[i+2])
        m_list.append(m)
        temp = []
        temp.append(a)
        temp.append(b)
        temp.append(m)
        equations.append(temp)
    
    apply_CRT(equations, m_list)
