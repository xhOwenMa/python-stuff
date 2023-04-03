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

def is_prime2(n):
  """
  fact: besides 2 and 3, all primes have the form 6k+1 or 6k-1. So this algorithm only looks at numbers of this form
  
  n : int
  return True if n is prime
  """
  if n == 2:
    return True
  if n == 3:
    return True
  if n % 2 == 0:
    return False
  if n % 3 == 0:
    return False

  i = 5
  w = 2

  while i * i <= n:
    if n % i == 0:
      return False

    i += w
    w = 6 - w

  return True
