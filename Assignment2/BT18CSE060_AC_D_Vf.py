import sys
import socket
from Crypto.Random import random
from Crypto.Hash import SHA256

from BT18CSE060_AC_D_helper import multiplicative_inverse

def activate():

    port = 8001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a server socket

    s.bind(('', port))           #an empty string in ip makes the server listen to requests coming from other computers on the network

    print("#########################################")

    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(1)
    print("Verifier is listening")


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

        msg = c.recv(1024)
        data = msg.decode()

        M, S1, S2 = data.split(':')

        with open("DSS_public_keys","r") as f:                 #getting pulic key
            for line in f:
                e1,e2,p,q = line.split(' ')
        
        e1 = int(e1)
        p = int(p)
        e2 = int(e2)
        q = int(q)

        S1 = int(S1)
        S2 = int(S2)

        S2_inv = multiplicative_inverse(S2, q)
        hash_m = SHA256.new(M.encode()).hexdigest()

        a = int(hash_m, 16) * S2_inv
        a = a%q
        temp1 = pow(e1,a, p)%q
        
        b = S1 * S2_inv
        b = b%q
        temp2 = pow(e2, b, p)%q

        V = (temp1 * temp2)%q

        if V%q == S1%q:

            c.send("Authenticated your message".encode())
            print("Message verified succesfully")
            print(f"Alice sent message :: {M}")
            reply = "Got your Message, Thank you!"
            c.send(reply.encode('utf-8'))
        
        else:

            print("Signatur is invalid, Message access denied!")
            c.send("Authentication of message failed!".encode())
            c.send("Please send with correct signature".encode())

        print("#########################################")


if __name__ == "__main__":

    activate()
