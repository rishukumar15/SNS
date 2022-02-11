# Code for 2 Round fistal cypher

import sys
import socket
from BT18CSE060_SE_Z_util import encrypt
from BT18CSE060_SE_Z_util import convert_string_to_binary


    
def run(plain_txt):
    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'

    port = 8001

    # connect to the server on local computer
    cl.connect((host, port))

    print('---------------------------------------------------------------')

    print(cl.recv(1024).decode())

    print(f"The Entered Plain Text is: {plain_txt}")

    bin_frmt = convert_string_to_binary(plain_txt)

    if len(bin_frmt)%2 == 1:        #odd size 
        bin_frmt.append(0)          #append dummy character
    
    ct_bin = encrypt(bin_frmt)

    print("Message encrypted, sending it to Bob")

    ct = ""

    for x in ct_bin:

        ch = str(x)
        ct += ch

    cl.send(ct.encode("utf-8"))

    ans = cl.recv(1024)
    print("Bob replied: ", end='')
    print(ans.decode())

    cl.close()

    print("connection closed")

    print('----------------------------------------------------------------------')


if __name__ == "__main__":

    plain_txt = sys.argv[1]

    run(plain_txt)