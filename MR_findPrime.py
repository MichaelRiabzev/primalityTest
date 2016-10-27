# Written by Michael Riabzev
# RiabzevMichael@gmail.com

import random
import time
import sys

def modular_exp(x,e,n):
    """
    return x^e mod n
    """
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X*X) % n
            E = E/2
        else:
            Y = (X*Y) % n
            E = E - 1
    
    return Y

def is_prime_MR(n):
    """
    return True iff n is prime (with high probability)
    """
    
    """
    factor n-1 to a power of 2 and an odd integer s
    """
    t=0 #The power of 2 in the exponent
    s=n-1
    while s%2 == 0:
        t+=1
        s=s/2

    """
    Test using a random element
    """
    for i in range(10):
        while True:
            x = random.randrange(2,n)

            if modular_exp(x,n-1,n) != 1 : return False

            x_curr = modular_exp(x,s,n)
            if x_curr == 1 : continue

            x_next = x_curr**2 % n
            while x_next != 1:
                x_curr = x_next
                x_next = x_next**2 % n

            if x_curr != n-1 : return False

            return True

def genRandOdd(numBits):
    n=1
    for i in range(numBits):
        n = n*2
        n += random.randrange(2)
    return (n*2)+1

def genRandPrime(numBits):
    while True:
        n = genRandOdd(numBits)
        
        start = time.time()
      
        prime = False 
        for i in range(30): 
            prime = is_prime_MR(n)
            if((not prime) and (i > 0)): print i
            if not prime : break
        
        end = time.time()
        
        if prime: return (n,end-start)

if __name__ == "__main__":
    num_bits = int(sys.argv[1])
    print "searching for a prime of %d bits" % num_bits
    start = time.time()
    (p,mr_time)=genRandPrime(num_bits)
    end = time.time()
    print "found the prime p = %d" % p
    print "it took %f seconds, the MR test took %f seconds"%(end-start, mr_time)
