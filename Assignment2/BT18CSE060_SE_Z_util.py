import sys

def convert_string_to_binary(pt):

    binary_arr = []

    for ch in pt:

        asc_val = ord(ch)               #to get ascii value of character
        bin = format(asc_val, "b")      #to get binary representaton of that Ascii character

        bin_int = list(map(int, bin))   #to convert binary string into a list of int
        binary_arr.extend(bin_int)      #storing binary representation of string in binary_arr
    

    return binary_arr




def convert_binary_to_string(pt_bin):

    block_size = 7          #7 bits are required to convert a character in binary format

    ans = ""

    track = 0

    while track+7 <= len(pt_bin):

        temp = pt_bin[track:track+7]
        track = track + block_size

        ch_bin = list(map(str, temp))

        num = "".join(ch_bin)
        asc_val = int(num,2)
        ch = chr(asc_val)

        ans += str(ch)
    
    return ans



def xor(l,r):

    res = list(a^b for a,b in zip(l,r))
    return res




def half_split(pt_bin):             #take a plain text and spllit it in to l and r

    n = len(pt_bin)
    mid = n//2
    l = pt_bin[:mid]
    r = pt_bin[mid:]

    return l,r




def function(r,roll):           #take roll as input as use it in key generation

    bin = format(roll, "b")
    
    while len(bin) < len(r):
        temp = bin[::-1]
        bin = temp + bin
    
    n = len(r)
    res = bin[:n]

    key = list(map(int, res))

    ans = list(a^b for a,b in zip(key,r))

    return ans



def decrypt(ct_bin):

    l,r = half_split(ct_bin)
    rounds = 2                      #2 rounds cipher

    for i in range(rounds):

        temp = l
        f_value = function(l,60)
        l = xor(r,f_value)
        r = temp
    
    return l+r



def encrypt(pt_bin):

    l,r = half_split(pt_bin)
    rounds = 2                      #2 rounds cipher

    for i in range(rounds):

        temp = r
        f_value = function(r,60)
        r = xor(l,f_value)
        l = temp
    
    return l+r