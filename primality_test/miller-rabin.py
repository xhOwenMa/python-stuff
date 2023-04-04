import random
 
def power(x, y, p):
    """
    do modular exponentiation (x^y) mod p

    x : int
    y : int
    p : int
    """
     
    result = 1;
    x = x % p

    while (y > 0):
        result = result * x % p
        y -= 1
     
    return result
 
def mr_prime_test(d, n):
    """
    this is the Miller-Rabin primality test algorithm: testing if n is prime

    d : int, this is odd and d * 2^k = n-1
    n : int
    returns True if n is probably prime, False if n is composite
    """
     
    # Pick a random number in [2..n-2]
    a = random.randint(2, n - 2)
    wit = is_witness(a, n)
    if(wit):
        return False
    else:
        return True

def is_witness(a, n):
    """
    test if a is a Miller-Rabin witness for n

    a : int
    n : int
    returns True if a is a Miller-Rabin witness for n; False otherwise
    """

    d = n - 1
    while (d % 2 == 0):
        d //= 2

    x = power(a, d, n);
    if (x == 1 or x == n - 1):
        return False
    
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == n - 1):
            return False
 
    return True
 
def is_prime(n, k):
    """
    general driver function: calling the Miller-Rabin primality test k times, larger k makes the test more accurate

    n : int, the number to be tested
    k : int, how many times the Miller-Rabin test is called
    returns True if n is probably prime, False if n is composite
    """
     
    if (n <= 1 or n == 4):
        return False
    if (n == 2 or n == 3):
        return True
 
    #find d such that 2^k * d = n - 1
    d = n - 1
    while (d % 2 == 0):
        d //= 2
 
    # Iterate given number of 'k' times
    while(k):
        if (mr_prime_test(d, n) == False):
            return False
        k -= 1
 
    return True;

# testing code:
# num = 10585
# k = 10
# a = 15
# total_prime = 0

# for i in range(1, num):
#     if(is_prime(i, k)):
#         total_prime += 1
#         #print("{} ".format({i}))
# print("total number of primes less than {} is {}".format({num}, {total_prime}))

# print("\n is {} prime: {}".format({num}, {is_prime(num, k)}))
# print("\n is {} a Miller-Rabin witness for {}: {}".format({a}, {num}, {is_witness(a, num)}))