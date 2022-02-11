import sys
import socket
from Crypto.Random import random
from Crypto.Hash import SHA256

from BT18CSE060_AC_D_Kg import key_generation
from BT18CSE060_AC_D_helper import multiplicative_inverse

def run(message):

    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'

    port = 8001

    # connect to the server on local computer
    cl.connect((host, port))

    print('---------------------------------------------------------------')

    print(cl.recv(1024).decode())

    print(f"The Entered Message by Alice is: {message}")

    public_key, private_key = key_generation()


    e1 ,e2 ,p ,q = public_key
    d = private_key

    r = random.randint(1,q-1)           #choose a random number from 1 to q as r

    with open("DSS_public_keys","w") as f:
        f.write(" ".join(tuple(map(str,public_key))))               #write in file so bob(server) can acess the pubic key
    
    S1 = pow(e1, r, p)%q

    r_inv = multiplicative_inverse(r, q)

    hash_m = SHA256.new(message.encode()).hexdigest()

    temp = int(hash_m, 16) + d*S1

    S2 = (temp * r_inv)%q

    cl.send(":".join((message,str(S1),str(S2))).encode())       # send message in the form M:S1:S2    

    print("Alice sent message to Bob with the signature")

    ans = cl.recv(1024)
    print("Bob replied: ", end='')
    print(ans.decode())

    ans = cl.recv(1024)
    print("Bob replied: ", end='')
    print(ans.decode())

    cl.close()

    print("connection closed")

    print('----------------------------------------------------------------------')



if __name__ == "__main__":

    message = sys.argv[1]

    run(message)