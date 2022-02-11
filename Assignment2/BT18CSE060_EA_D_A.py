import sys
import socket
from Crypto.Random import random

from BT18CSE060_EA_D_Kg import key_generation

def run():

    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'

    port = 8001

    # connect to the server on local computer
    cl.connect((host, port))

    print('---------------------------------------------------------------')

    print(cl.recv(1024).decode())

    n, e, s, v = key_generation()

    rounds = 3

    public_value = (n, e, v, rounds)

    with open("public_vals","w") as f:
        f.write(" ".join(tuple(map(str,public_value))))               #write in file so bob(server) can acess the pubic key and values
    

    cl.send("File created to access Public values".encode())

    f = 0

    print("Verification starting.......")

    for i in range(rounds):

        r = random.randint(1,1000)

        x = pow(r,e,n)
        x_str = str(x)

        cl.send(x_str.encode("utf-8"))

        msg = cl.recv(1024)
        data = msg.decode()
        c = int(data)

        temp = pow(s,c)
        y = (temp * r)%n

        y_str = str(y)

        #print(y_str)
        cl.send(y_str.encode("utf-8"))

        reply = cl.recv(1024)
        reply_data = reply.decode()

        if reply_data == "Pass":

            print(f"Passed the test {i+1} successfully")
        
        else:

            print(f"Failed authentication at test {i+1}")
            f = 1
            break
    
    if f == 0:

        print("Verification of Alice done successfully")
    
    cl.close()

    print("connection closed")

    print('----------------------------------------------------------------------')



if __name__ == "__main__":

    run()
