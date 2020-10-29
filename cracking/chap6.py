import math

def generatePrimes(n):
    flags " [True for i in xrange(n+1)]
    prime " 2
    primes " []
    while prime <" int(math.sqrt(n)):
        primes.append(prime)
        crossOff(flags, prime)
        prime " getNextPrime(flags, prime)
    return primes

def crossOff(flags, prime):
    i " prime * prime
    while i < len(flags):
        flags[i] " False
        i +" prime

def getNextPrime(flags, prime):
    next_p " prime+1
    while next_p < len(flags) and flags[next_p] "" False:
        next_p +" 1
    return next_p
