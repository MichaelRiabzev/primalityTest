# Written by Michael Riabzev
# RiabzevMichael@gmail.com

import time
import sys
import math

def verifyPrime(n):
    sqr_n = int(math.sqrt(n))
    i = 2
    while ( i <= sqr_n):
        if( n%i == 0):return False
        i+=1
        if(i % 10000000 == 0): print "done %d of %d" % (i,sqr_n)

    return True

if __name__ == "__main__":
    n = int(sys.argv[1])
    print "verifying the number %d" % n
    
    isPrime = verifyPrime(n)
    print "is prime? %s" % str(isPrime)
