
import random, math

def is_prime(n):
    """
    n : int
    return True if n is prime
    """
  
    if n < 2:
        return False
    
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
        
    return True

def gen_prime(n):
    """
    return a random prime that is less than n
    """
    
    r = random.randint(2,n)
    while(is_prime(r) == False):
        r = random.randint(2,n)

    return r

def compute_str(x, e, N):
    """
    return the result string by doing the specified operation
    """

    s = ""
    y = []
    y.append(x)
    for i in range(0,100):
        s += str(y[i] % 2) # get the bit x_i
        y.append((y[i]**e) % N) # compute y_i+1

    return s


def main():
    # randomly generate prime p and q and p != q
    p = gen_prime(1000)
    q = gen_prime(1000)
    while(q == p):
        q = gen_prime(1000)

    # computes N and M
    N = p*q
    M = (p-1) * (q-1)

    # generate e
    e = random.randint(3,M)
    while(math.gcd(e,M) != 1):
        e = random.randint(3,M)

    # generate x
    x = random.randint(2,N)
    while(math.gcd(x,N) != 1):
        x = random.randint(2,N)

    print("p={}, q={}, e={}".format(p,q,e))

    s = compute_str(x, e, N)
    print("the result string is: {}".format(s))

if __name__ == "__main__":
    main()