import sys

def extended_euclidean(a,b):
    
    #Base Case
    if b == 0:
        return 1,0
    
    x1,y1 = extended_euclidean(b,a%b)

    y = x1 - (a//b) * y1
    x = y1

    return x,y

if __name__ == "__main__":
    input_list = sys.argv[1:]
    x2,y2 = extended_euclidean(int(input_list[0]),int(input_list[1]))
    print(x2,y2,end="")
   
