import sys
import socket
from Crypto.Random import random

def activate():

    port = 8001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a server socket

    s.bind(('', port))           #an empty string in ip makes the server listen to requests coming from other computers on the network

    print("#########################################")

    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(1)
    print("Bob is listening")


    

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        # Establish connection with client.
        c, addr = s.accept()
        print('----------------------------------------------------------')
        print('Got connection from', addr)
        print('----------------------------------------------------------')


        # send a thank you message to the client.
        c.send('Thank you for connecting'.encode())

        
        conf = c.recv(1024)
        conf_dec = conf.decode()
        print(conf_dec)


        with open("public_vals","r") as f:                 #getting pulic key
            for line in f:
               n, e, v, rounds = line.split(' ')
        
        n = int(n)
        e = int(e)
        v = int(v)
        rounds = int(rounds)

        f = 0


        print(f"Authenticating and verifying the Alice for {rounds} rounds")

        for i in range(rounds):

            msg = c.recv(1024)
            data = msg.decode()
            x = int(data)
            

            #print("here")
            challenge = random.randint(1, e)

            c_str = str(challenge)

            c.send(c_str.encode("utf-8"))

            msg1 = c.recv(1024)
            data1 = msg1.decode()
            y = int(data1)

            a = pow(y,e,n)
            b = pow(v,challenge,n)

            a = int(a)
            b = int(b)


            res = (a*b)%n
            
            x = x%n

            if res == x :

                print(f"Pass the test {i+1} of verification")
                c.send("Pass".encode("utf-8"))
            
            else:
                print(f"Failed test {i+1}, Authentication denied!")
                c.send("Fail".encode("utf-8"))
        
        print("Alice can now send the messages freely")

        print("#########################################")



if __name__ == "__main__":

    activate()
