import sys
import socket
from des import DesKey

# Defining some shared variables
IDa = "a86b1821f84e6d82"                # Alice ID Shared with everyone of 128 bits
IDb = "f1df45ae8382bda1"                # Bob ID Shared with everyone of 128 bits
R = "1623868025931781"                  # Common nonce of 128 bits
Rb = "F)J@NcRfUjXn2r5u"                 # Nonce between Alice and KDC of 128 bits


kb = "JaNdRgUk"                 # Shared key between Bob and KDC

def activate():

    port = 8002

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

        # Establish connection with Alice.
        c, addr = s.accept()
        print('----------------------------------------------')
        print('Got connection from', addr)
        print('----------------------------------------------')

        # send a thank you message to the client.
        c.send('Thank you Alice for connecting'.encode())

        alice_details_enc = c.recv(1024)

        # Encrypt the IDa, IDb, R, Rb using Kb
        details_sent = IDa + ":" + IDb + ":" + R + ":" + Rb
        key = DesKey(bytes(kb, 'utf8'))
        bob_details_enc = key.encrypt(bytes(details_sent, 'utf8'), padding=True)

        kdc_ip = '127.0.0.1'

        port_kdc = 8003

        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect((kdc_ip, port_kdc))

        print("Established Connection with KDC")

        s1.send(alice_details_enc)
        print(s1.recv(1024).decode("utf-8"))

        s1.send(bob_details_enc)
        print(s1.recv(1024).decode("utf-8"))

        # Receive session key from KDC
        session_key_for_alice = s1.recv(1024)
        session_key_for_bob = s1.recv(1024)

        print("Recieved Session Keys for Both Alice and Bob")

        c.send(session_key_for_alice)

        print("Forwaded the session key details to alice")

        datas = key.decrypt(session_key_for_bob).decode("utf-8")
        _, session_key = datas.split(':')

        session_key = session_key[:len(session_key)-2]


        shared_key = DesKey(bytes(session_key, "utf8"))
        print("Shared Key Established......")

        enc_msg = c.recv(1024)
        msg = shared_key.decrypt(enc_msg, padding=True).decode("utf-8")

        msg = msg.rstrip()

        print("Decrypting message.......")

        print(f"Message sent by Alice: {msg}")

        reply = "Got your Message, Thank you!"
        c.send(reply.encode('utf-8'))

        print("#########################################")
    

if __name__ == "__main__":

    activate()
            



        




