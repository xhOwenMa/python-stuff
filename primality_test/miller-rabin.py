import random
 
def mr_prime_test(q, n):
    """
    this is the Miller-Rabin primality test algorithm: testing if n is prime

    q : int
    n : int
    return True if n is probably prime, False if n is composite
    """
     
    # Pick a random number in [2..n-2]
    a = random.randint(2, n - 2)
    wit = is_witness(a, q, n)
    if(wit):
        return False
    else:
        return True

def is_witness(a, q, n):
    """
    test if a is a Miller-Rabin witness for n

    a : int
    q : int
    n : int
    return True if a is a Miller-Rabin witness for n; False otherwise
    """

    x = pow(a, q, n); # modular exponentiation: a^d mod n
    if (x == 1 or x == n - 1):
        return False
    
    while (q != n - 1):
        x = (x * x) % n
        q *= 2
        if (x == n - 1):
            return False
 
    return True
 
def is_prime(n, r):
    """
    general driver function: calling the Miller-Rabin primality test k times, larger k makes the test more accurate

    n : int, the number to be tested
    r : int, how many times the Miller-Rabin test is called
    return True if n is probably prime, False if n is composite
    """
     
    if (n <= 1 or n == 4):
        return False
    if (n == 2 or n == 3):
        return True
 
    q = find_q(n)
 
    # Iterate r times
    while(r):
        if (mr_prime_test(q, n) == False):
            return False
        r -= 1
 
    return True;

def find_q(n):
    """
    return q such that 2^k * q = n-1
    """
    q = n - 1
    while(q % 2 == 0):
        q //= 2

    return q

def num_prime(n, r):
    """
    return how many primes there are that are less or equal to n
    """
    num = 0
    for i in range(2, n+1):
        if(is_prime(i, r)):
            num += 1
    
    return num


# testing code:
n = 100000
r = 10 # number of tests, higher r will make the result more reliable
a = 15 # to test if a is a Miller-Rabin witness for n
q = find_q(n)

print("total number of primes less than {} is {}".format(n, num_prime(n, r)))

print("\n is {} prime: {}".format(n, is_prime(n, r)))
print("\n is {} a Miller-Rabin witness for {}: {}".format(a, n, is_witness(a, q, n)))