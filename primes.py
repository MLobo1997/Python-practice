

def insertOrder (n, l):

    i = 0
    for num in l:
        if num > n:
            l.insert(i,n)
            break
        elif num == n:
            break
        i=i+1
    return l
'''
def primeGen (lim):
    nonPrime=[]
    primes=list(range(2,lim))
    i=0

    for num in primes: 
        if not(num in nonPrimeInd):
            pos=i
            for num2 in primes:
                
                if pos 
                
        i=i+1



def primesfact (n):
    factors=[]

    if n != 1:
        primesdiv(n)

        primesfact(n)

    return factors

    '''
