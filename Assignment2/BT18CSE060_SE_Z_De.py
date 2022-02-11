import sys
import socket
from BT18CSE060_SE_Z_util import decrypt
from BT18CSE060_SE_Z_util import convert_binary_to_string



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

        expr = c.recv(1024)
        msg_bin = expr.decode()
        ct_bin = list(map(int, msg_bin))
        pt_bin = decrypt(ct_bin)
        msg = convert_binary_to_string(pt_bin)
        print("getting message....")
        print(f"Alice sent message :: {msg}")
        reply = "Got your Message, Thank you!"
        c.send(reply.encode('utf-8'))
        print("#########################################")




if __name__ == "__main__":

    activate()
            