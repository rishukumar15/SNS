import sys
import socket
from des import DesKey

# Defining some shared variables
IDa = "a86b1821f84e6d82"                # Alice ID Shared with everyone of 128 bits
IDb = "f1df45ae8382bda1"                # Bob ID Shared with everyone of 128 bits
R = "1623868025931781"                  # Common nonce of 128 bits
Ra = "McQfTjWnZr4u7x!A"                 # Nonce between Alice and KDC of 128 bits


ka = "r5x/A?(G"                 # Shared key between Alice and KDC


def run(message):
    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'

    port = 8002

    # connect to the server on local computer
    cl.connect((host, port))

    print('----------------------------------------------')

    print("Alice is in running status...")

    print(cl.recv(1024).decode())

    # Encrypt the IDa, IDb, R, Ra using Ka
    details_sent = IDa + ":" + IDb + ":" + R + ":" + Ra
    key = DesKey(bytes(ka, 'utf8'))
    enc_details = key.encrypt(bytes(details_sent, 'utf8'), padding=True)

    cl.send(enc_details)

    print("Connection details sent to Bob....")

    #Recieve session key from Bob
    encrypted_session_key = cl.recv(1024)

    print("Recieved Session Key from KDC")

    # Decrypt session key
    session_key_datas = key.decrypt(encrypted_session_key).decode("utf8")
    _, session_key = session_key_datas.split(':')
    print("Session Key decrypted by Alice")

    session_key = session_key[:len(session_key)-2]

    #Sending message
    key_shared = DesKey(bytes(session_key, 'utf8'))
    enc_msg = key_shared.encrypt(bytes(message, 'utf8'), padding=True)

    print("Connection established successfully between Alice and Bob...")

    cl.send(enc_msg)

    print("Message sent to Bob.......")

    ans = cl.recv(1024)
    print("Bob replied: ", end='')
    print(ans.decode())

    cl.close()

    print("connection closed")

    print('----------------------------------------------')





if __name__ == "__main__":

    message = sys.argv[1]           #msg to send from Alice to Bob

    run(message)

