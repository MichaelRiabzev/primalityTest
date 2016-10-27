# primalityTest
Miler-Rabin VS. Schoolbook primality tests : for educational purposes

Usage of SchoolBook_PrimalityTest.py:
```bash
python SchoolBook_PrimalityTest.py <a number to test>
```
It will output eventually whether the argument is prime or not.

Usage of MR_findPrime.py
```bash
python MR_findPrime.py <number of bits>
```
This script will search for a prime of the size <number of bits>+2, where both lsb and msb are allways on, that is where the +2 comes from.

examples:
```bash
> python MR_findPrime.py 50
searching for a prime of 50 bits
found the prime p = 2266828492608257
it took 0.012608 seconds, the MR test took 0.004651 seconds

> python SchoolBook_PrimalityTest.py 2266828492608257
verifying the number 2266828492608257
done 10000000 of 47611222
done 20000000 of 47611222
done 30000000 of 47611222
done 40000000 of 47611222
is prime? True
```
