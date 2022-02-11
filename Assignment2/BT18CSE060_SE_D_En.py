import sys
import socket
from des import DesKey





def convert_string_to_binary(pt):

    binary_arr = []

    for ch in pt:

        asc_val = ord(ch)               #to get ascii value of character
        bin = format(asc_val, "08b")      #to get binary representaton of that Ascii character

        binary_arr.append(bin)
    

    return binary_arr




def get_blocks_of_r_size(pt_txt, r):

    n = r
    blocks = [pt_txt[i:i+n] for i in range(0, len(pt_txt), n)]
    return blocks



def CTR_encrypt(plain_txt):

    res = get_blocks_of_r_size(plain_txt, 8)

    iv = "12345678"
    ky = "Rishu123"

    print("starting encryption......")

    cypher_txt = ""

    for block in res:

        key = DesKey(bytes(ky, 'utf-8'))
        enc = key.encrypt(bytes(iv, 'utf-8'))


        lt  = list(enc)             #returns a list of ascill value of each letter


        lt_bin = []

        for asc_val in lt:

           x = format(asc_val, "08b")       #to get binary format in 8 bits
           lt_bin.append(x)
        
      

        block_bin = convert_string_to_binary(block)


        for x,y in zip(lt_bin, block_bin):

            ans = int(x,2) ^ int(y,2)
            cypher_txt += str(ans)
            cypher_txt += ':'


        iv_val = int(iv)                    #counter increment
        iv_val += 1
        iv = str(iv_val)
    
    cypher_txt = cypher_txt[:len(cypher_txt) - 1]
    
    return cypher_txt
    

       



def run(plain_txt):

    cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'

    port = 8001

    # connect to the server on local computer
    cl.connect((host, port))

    print('---------------------------------------------------------------')

    print(cl.recv(1024).decode())

    print(f"The Entered Plain Text is: {plain_txt}")

    cypher_txt = CTR_encrypt(plain_txt)

    print("Message encrypted, sending it to server")

    cl.send(cypher_txt.encode("utf-8"))

    ans = cl.recv(1024)
    print("Bob replied: ", end='')
    print(ans.decode())

    cl.close()

    print("connection closed")

    print('----------------------------------------------------------------------')





if __name__ == "__main__":

    pt =  sys.argv[1]

    while len(pt) % 8 != 0:

        pt += " "                           #Padding space in last to make it size of multiple of 8

    run(pt)