def is_prime(i):
  """
  test if i is prime
  
  i : int
  """
  
    if i < 2:
        return False
    
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            return False
        
    return True
