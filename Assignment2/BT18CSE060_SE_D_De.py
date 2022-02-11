import sys
import socket
from des import DesKey




def CTR_decrypt(cypher_txt):

    
    iv = "12345678"                 # initialisation vector
    ky = "Rishu123"                 # key for des

    plain_txt = ""

    cypher_txt = cypher_txt.split(':')

    print("starting decryption......")

    for i in range(0,len(cypher_txt),8):

        lt_bin = []

        for j in range(i,i+8):

            x = format(int(cypher_txt[j]), "08b")           #binary format of each block of Cypher Text
            lt_bin.append(x)
        
        key = DesKey(bytes(ky, 'utf-8'))
        enc = key.encrypt(bytes(iv, 'utf-8'))

        lt = list(enc)

        lt = [format(x, "08b") for x in lt] 

        for x,y in zip(lt_bin, lt):

            ans = int(x,2) ^ int(y,2)
            ch = chr(ans)
            plain_txt += str(ch)
        
        iv_val = int(iv)
        iv_val += 1
        iv = str(iv_val)

    return plain_txt



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

        msg = c.recv(1024)
        msg_ct = msg.decode()
        plain_txt = CTR_decrypt(msg_ct)
        plain_txt = plain_txt.rstrip()
        print("getting message....")
        print(f"Alice sent message :: {plain_txt}")
        reply = "Got your Message, Thank you!"
        c.send(reply.encode('utf-8'))
        print("#########################################")




if __name__ == "__main__":

    activate()

