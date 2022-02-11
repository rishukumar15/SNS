import sys
import socket
from des import DesKey
import string
import random

# Defining some shared variables
IDa = "a86b1821f84e6d82"                # Alice ID Shared with everyone of 128 bits
IDb = "f1df45ae8382bda1"                # Bob ID Shared with everyone of 128 bits
R = "1623868025931781"                  # Common nonce of 128 bits

K = 64

ka = "r5x/A?(G"                 # Shared key between Alice and KDC
kb = "JaNdRgUk"                 # Shared key between Bob and KDC

# Session key generator
def generate_session_key():
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = K//8))
    return res


def Kda_working():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a server socket

    port = 8003

    s.bind(('', port))           #an empty string in ip makes the server listen to requests coming from other computers on the network

    print("#########################################")

    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(1)
    print("KDC is in listening mode")

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        # Establish connection with Alice.
        c, addr = s.accept()
        print('--------------------------------------------------')
        print('Got connection from', addr)
        print('--------------------------------------------------')

        alice_details_enc = c.recv(1024)

        print("Alice deatils recieved")
        c.send("Alice details recieved successfully by KDC".encode("utf-8"))

        key_a = DesKey(bytes(ka, "utf8"))
        alice_details = key_a.decrypt(alice_details_enc).decode()

        datas_list = alice_details.split(':')
        Ra = datas_list[3]

        print("Decrypted the value of Ra from alice details")

        bob_details_enc = c.recv(1024)

        print("Bob deatils recieved")
        c.send("Bob details recieved successfully by KDC".encode("utf-8"))

        key_b = DesKey(bytes(kb, "utf8"))
        bob_details = key_b.decrypt(bob_details_enc).decode()

        datas_list_b = bob_details.split(':')
        Rb = datas_list_b[3]

        print("Decrypted the value of Rb from bob details")

        # Generate session key 
        session_key = generate_session_key()

        print("session_key generated is: ", session_key)

        print("Generated Session key for Alice and Bob")

        alice_session  = Ra + ":" + session_key
        bob_session = Rb + ":" + session_key

        alice_sess_enc = key_a.encrypt(bytes(alice_session, 'utf8'), padding=True)
        bob_sess_enc = key_b.encrypt(bytes(bob_session, 'utf8'), padding=True)

        c.send(alice_sess_enc)
        print("Session key details of Alice sent")

        c.send(bob_sess_enc)
        print("Session key details of Bob sent")

        print("Connection established between Bob and Alice!")

        print("----------------------------------------------")
        

if __name__ == "__main__":

    Kda_working()
