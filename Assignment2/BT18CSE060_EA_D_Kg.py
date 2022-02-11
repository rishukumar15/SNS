from Crypto.Util import number
import random

from BT18CSE060_EA_D_util import get_RRSM_set, multiplicative_inverse

P_BITS = 10
Q_BITS = 6

def key_generation():

    p = number.getPrime(P_BITS)         #generate a random prime number of size P_BITS
    q = number.getPrime(Q_BITS)         #generate a random prime number of size Q_BITS

    n = p*q 

    phi_n = (p-1)*(q-1)                 #phi value of N

    rrsm = get_RRSM_set(phi_n)          #to get RRSM set of phi_n

    e = random.choice(rrsm)             #to get exponential e (such that it is co-prime with phi_n) randomly from RRSM set

    rrsm_n = get_RRSM_set(n)

    s = random.choice(rrsm_n)                     #secret key so it belongs to Z*(n)

    temp = pow(s,e,n)

    v = multiplicative_inverse(temp, n)     #public_key

    return n, e, s, v






