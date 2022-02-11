from Crypto.Util import number
import random
from BT18CSE060_AC_D_helper import prime_factors, primitive_roots, is_prime_number


P_BITS = 40             #bit size of prime P

def key_generation():

    p = number.getPrime(P_BITS)         #generate a random prime number of size P_BITS
    p_facs = prime_factors(p-1)
    q = random.choice(p_facs)          #choose a random pime number from prime factors list as q

    print(f"P value :: {p}")
    print(f"Q value :: {q}")

    e0 = primitive_roots(p)             #choose e0 as a generator from Zp*

    # e1 is qth root of 1modp
    e1 = pow(e0, (p-1)//q, p)

    d = random.randint(1,q-1)

    e2 = pow(e1,d,p)

    public_key = (e1,e2,p,q)
    private_key = d

    return public_key, private_key
